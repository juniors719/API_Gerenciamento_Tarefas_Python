from fastapi import FastAPI
from fastapi.responses import HTMLResponse

from fast_zero.routers import auth, todos, users
from fast_zero.schemas import (
    MessageSchema,
)

app = FastAPI(
    title='API de Gerenciamento de Tarefas',
    version="1.0.0",
    description="""
    Um projeto desenvolvido com FastAPI e gerenciado pelo Poetry,
    que fornece uma API para o gerenciamento de tarefas e usuários.
    A aplicação permite a criação, leitura, atualização e exclusão
    (CRUD) de tarefas, além de funcionalidades completas para
    a administração de usuários.
    """,
    contact={
        "name": "Djalma Júnior",
        "email": "junior.silva@alu.ufc.br",
        "url": "https://github.com/juniors719/API_Gerenciamento_Tarefas_Python",
    },
    license_info={
        "name": "GNU General Public License v3.0",
        "url": "https://www.gnu.org/licenses/gpl-3.0.html",
    },
)

app.include_router(users.router)
app.include_router(auth.router)
app.include_router(todos.router)


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
