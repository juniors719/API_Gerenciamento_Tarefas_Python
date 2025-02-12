from http import HTTPStatus

from fastapi import Depends, FastAPI, HTTPException
from fastapi.responses import HTMLResponse
from sqlalchemy import select
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from fast_zero.database import get_session
from fast_zero.models import User
from fast_zero.schemas import (
    MessageSchema,
    UserList,
    UserPublic,
    UserSchema,
)

app = FastAPI()


@app.get('/', response_model=MessageSchema)
def read_root():
    return {'message': 'Hello World!'}


@app.get('/ola_mundo', response_class=HTMLResponse)
def ola_mundo_exercise():
    return """
        <html>
        <head>
            <title>Nosso olá mundo!</title>
        </head>
        <body>
            <h1> Olá Mundo </h1>
        </body>
        </html>
    """


@app.post(
    '/users',
    status_code=HTTPStatus.CREATED,
    response_model=UserPublic,
    summary='Cria um usuário',
    description='Adiciona um usuário ao banco de dados',
)
def create_user(user: UserSchema, session: Session = Depends(get_session)):
    db_user = session.scalar(
        select(User).where(
            (User.email == user.email) | (User.username == user.username)
        )
    )
    if db_user:
        if db_user.username == user.username:
            raise HTTPException(
                status_code=HTTPStatus.BAD_REQUEST,
                detail='Username already registered',
            )
        elif db_user.email == user.email:
            raise HTTPException(
                status_code=HTTPStatus.BAD_REQUEST,
                detail='Email already registered',
            )
    db_user = User(
        username=user.username, email=user.email, password=user.password
    )
    session.add(db_user)
    session.commit()
    session.refresh(db_user)
    return db_user


@app.get(
    '/users/',
    response_model=UserList,
    summary='Lista todos os usuários',
    description='Retorna uma lista com todos os usuários cadastrados',
)
def read_users(
    limit: int = 10, skip: int = 0, session: Session = Depends(get_session)
):
    users = session.scalars(select(User).limit(limit).offset(skip))
    return {'users': users}


@app.get(
    '/users/{user_id}',
    response_model=UserPublic,
    summary='Obtém um usuário específico',
    description='Retorna os detalhes de um usuário pelo ID',
)
def read_user(user_id: int, session=Depends(get_session)):
    user = session.scalar(select(User).where(User.id == user_id))
    if not user:
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND,
            detail='User not found',
        )
    return user
    


@app.put(
    '/users/{user_id}',
    response_model=UserPublic,
    status_code=HTTPStatus.OK,
    summary='Atualiza um usuário existente',
    description='Atualiza os detalhes de um usuário pelo ID',
)
def update_user(
    user_id: int, user: UserSchema, session: Session = Depends(get_session)
):

    db_user = session.scalar(select(User).where(User.id == user_id))
    if not db_user:
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND, detail='User not found'
        )

    try:
        db_user.username = user.username
        db_user.password = user.password
        db_user.email = user.email
        session.commit()
        session.refresh(db_user)

        return db_user

    except IntegrityError: 
        raise HTTPException(
            status_code=HTTPStatus.CONFLICT, 
            detail='Username or Email already exists'
        )


@app.delete(
    '/users/{user_id}',
    status_code=HTTPStatus.OK,
    response_model=MessageSchema,
    summary='Deleta um usuário',
    description='Deleta um usuário pelo ID',
)
def delete_user(user_id: int, session: Session = Depends(get_session)):
    db_user = session.scalar(select(User).where(User.id == user_id))
    if not db_user:
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND,
            detail='User not found',
        )
    session.delete(db_user)
    session.commit
    return {'message': 'User deleted'}
