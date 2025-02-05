from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()


@app.get('/')
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
