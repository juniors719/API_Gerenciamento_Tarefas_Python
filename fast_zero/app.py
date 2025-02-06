from http import HTTPStatus

from fastapi import FastAPI, HTTPException
from fastapi.responses import HTMLResponse

from fast_zero.schemas import (
    MessageSchema,
    UserDB,
    UserList,
    UserPublic,
    UserSchema,
)

app = FastAPI()

database = []  # provisório para simular um banco de dados


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
def create_user(user: UserSchema):
    user_with_id = UserDB(id=len(database) + 1, **user.model_dump())
    database.append(user_with_id)
    return user_with_id


@app.get(
    '/users/',
    response_model=UserList,
    summary='Lista todos os usuários',
    description='Retorna uma lista com todos os usuários cadastrados',
)
def read_users():
    return {'users': database}


@app.get(
    '/users/{user_id}',
    response_model=UserPublic,
    summary='Obtém um usuário específico',
    description='Retorna os detalhes de um usuário pelo ID',
)
def read_user(user_id: int):
    if user_id < 1 or user_id > len(database):
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND,
            detail='User not found',
        )
    user = database[user_id - 1]
    return user


@app.put(
    '/users/{user_id}',
    response_model=UserPublic,
    status_code=HTTPStatus.OK,
    summary='Atualiza um usuário existente',
    description='Atualiza os detalhes de um usuário pelo ID',
)
def update_user(user_id: int, user: UserSchema):
    if user_id < 1 or user_id > len(database):
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND,
            detail='User not found',
        )
    user_with_id = UserDB(id=user_id, **user.model_dump())
    database[user_id - 1] = user_with_id
    return user_with_id


@app.delete(
    '/users/{user_id}',
    status_code=HTTPStatus.OK,
    response_model=MessageSchema,
    summary='Deleta um usuário',
    description='Deleta um usuário pelo ID',
)
def delete_user(user_id: int):
    if user_id < 1 or user_id > len(database):
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND,
            detail='User not found',
        )
    database.pop(user_id - 1)
    return {'message': 'User deleted'}
