from http import HTTPStatus


def test_get_token(client, user):
    response = client.post(
        '/auth/token',
        data={'username': user.email, 'password': user.clean_password},
    )
    token = response.json()
    assert response.status_code == HTTPStatus.OK
    assert token['token_type'] == 'Bearer'
    assert 'access_token' in token


def test_get_token_not_found(client, user):
    response = client.post(
        '/auth/token',
        data={
            'username': 'email_errado@test.com',
            'password': user.clean_password,
        },
    )
    assert response.status_code == HTTPStatus.BAD_REQUEST
