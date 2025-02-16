from http import HTTPStatus
from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from sqlalchemy.sql import select

from fast_zero.database import get_session
from fast_zero.models import Todo, User
from fast_zero.schemas import (
    FilterTodo,
    MessageSchema,
    TodoList,
    TodoPublic,
    TodoSchema,
    TodoUpdate,
)
from fast_zero.security import get_current_user

T_Session = Annotated[Session, Depends(get_session)]
T_CurrentUser = Annotated[User, Depends(get_current_user)]
T_FilterTodo = Annotated[FilterTodo, Query()]

router = APIRouter(
    prefix='/todos',
    tags=['todos'],
)


@router.post(
    '/',
    response_model=TodoPublic,
    summary='Cria um novo todo',
    description='Cria um novo todo para o usuário autenticado.',
    status_code=HTTPStatus.CREATED,
)
def create_todo(
    user: T_CurrentUser,
    session: T_Session,
    todo: TodoSchema,
):
    db_todo = Todo(
        title=todo.title,
        description=todo.description,
        state=todo.state,
        user_id=user.id,
    )
    session.add(db_todo)
    session.commit()
    session.refresh(db_todo)

    return db_todo


@router.get(
    '/',
    response_model=TodoList,
    summary='Lista todos os todos',
    description='Lista todos os todos do usuário autenticado.',
)
def list_todos(
    user: T_CurrentUser, session: T_Session, todo_filter: T_FilterTodo
):
    query = select(Todo).where(Todo.user_id == user.id)

    if todo_filter.title:
        query = query.filter(Todo.title.contains(todo_filter.title))

    if todo_filter.description:
        query = query.filter(
            Todo.description.contains(todo_filter.description)
        )

    if todo_filter.state:
        query = query.filter(Todo.state == todo_filter.state)

    todos = session.scalars(
        query.offset(todo_filter.offset).limit(todo_filter.limit)
    ).all()

    return {'todos': todos}


@router.delete('/{todo_id}', response_model=MessageSchema)
def delete_todo(todo_id: int, session: T_Session, user: T_CurrentUser):
    todo = session.scalar(
        select(Todo).where(Todo.user_id == user.id, Todo.id == todo_id)
    )

    if not todo:
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND, detail='Task not found.'
        )

    session.delete(todo)
    session.commit()

    return {'message': 'Task has been deleted successfully.'}


@router.patch(path='/{todo_id}', response_model=TodoPublic)
def patch_todo(
    todo_id: int, session: T_Session, user: T_CurrentUser, todo: TodoUpdate
):
    db_todo = session.scalar(
        select(Todo).where(Todo.id == todo_id, Todo.user_id == user.id)
    )
    if not db_todo:
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND, detail='Task not found.'
        )
    for key, value in todo.model_dump(exclude_unset=True).items():
        setattr(db_todo, key, value)
    session.add(db_todo)
    session.commit()
    session.refresh(db_todo)

    return db_todo
