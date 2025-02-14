from fastapi import FastAPI
from fastapi.responses import HTMLResponse

from fast_zero.routers import auth, users
from fast_zero.schemas import (
    MessageSchema,
)

app = FastAPI()
app.include_router(users.router)
app.include_router(auth.router)


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
