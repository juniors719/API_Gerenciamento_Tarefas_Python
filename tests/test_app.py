from http import HTTPStatus


def test_read_root_deve_retornar_ok_e_hello_world(client):
    response = client.get('/')
    assert response.status_code == HTTPStatus.OK
    assert response.json() == {'message': 'Hello World!'}


def test_exercicio_ola_mundo(client):
    response = client.get('/ola_mundo')
    assert response.status_code == HTTPStatus.OK
    assert '<h1> Olá Mundo </h1>' in response.text
