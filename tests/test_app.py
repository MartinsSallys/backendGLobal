from http import HTTPStatus

from fastapi.testclient import TestClient

from tabacaria_pj.app import app

client = TestClient(app)


def test_ola():
    client = TestClient(app)

    response = client.get('/')
    assert response.json() == {'message': 'ola mundo'}
    assert response.status_code == HTTPStatus.OK


def test_create_user(client):
    response = client.post(
        '/users/',
        json={
            'username': 'testuser',
            'email': 'testuser@example.com',
            'password': 'testpassword',
        },
    )
    assert response.status_code == HTTPStatus.CREATED
    assert response.json()['username'] == 'testuser'
    assert response.json()['email'] == 'testuser@example.com'
