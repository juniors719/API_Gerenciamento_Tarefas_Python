from http import HTTPStatus


def test_read_root_deve_retornar_ok_e_hello_world(client):
    response = client.get('/')
    assert response.status_code == HTTPStatus.OK
    assert response.json() == {'message': 'Hello World!'}


def test_exercicio_ola_mundo(client):
    response = client.get('/ola_mundo')
    assert response.status_code == HTTPStatus.OK
    assert '<h1> Olá Mundo </h1>' in response.text


def test_create_user(client):
    response = client.post(
        '/users',
        json={
            'username': 'johndoe',
            'email': 'johndoe@example.com',
            'password': '12345678',
        },
    )
    # O status_code esperado é HTTPStatus.CREATED
    assert response.status_code == HTTPStatus.CREATED
    # O JSON retornado deve ser igual ao esperado (UserPublic)
    assert response.json() == {
        'id': 1,
        'username': 'johndoe',
        'email': 'johndoe@example.com',
    }


def test_read_users(client):
    response = client.get('/users/')
    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        'users': [
            {'id': 1, 'username': 'johndoe', 'email': 'johndoe@example.com'}
        ]
    }


def test_read_user(client):
    response = client.get('/users/1')
    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        'id': 1,
        'username': 'johndoe',
        'email': 'johndoe@example.com',
    }


def test_read_user_not_found(client):
    response = client.get('/users/2')
    assert response.status_code == HTTPStatus.NOT_FOUND
    assert response.json() == {'detail': 'User not found'}


def test_update_user(client):
    response = client.put(
        '/users/1',
        json={
            'username': 'johndoe_alterado',
            'email': 'johndoealterado@example.com',
            'password': '12345678',
        },
    )
    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        'id': 1,
        'username': 'johndoe_alterado',
        'email': 'johndoealterado@example.com',
    }


def test_update_user_not_found(client):
    response = client.put(
        '/users/2',
        json={
            'username': 'johndoe_alterado',
            'email': 'johndoealterado@example.com',
            'password': '12345678',
        },
    )
    assert response.status_code == HTTPStatus.NOT_FOUND
    assert response.json() == {'detail': 'User not found'}


def test_delete_user(client):
    response = client.delete('/users/1')
    assert response.status_code == HTTPStatus.OK
    assert response.json() == {'message': 'User deleted'}


def test_delete_user_not_found(client):
    response = client.delete('/users/2')
    assert response.status_code == HTTPStatus.NOT_FOUND
    assert response.json() == {'detail': 'User not found'}
