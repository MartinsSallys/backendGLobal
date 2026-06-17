from http import HTTPStatus

from fastapi.testclient import TestClient

from tabacaria_pj.app import app

client = TestClient(app)


def test_create_user(client):
    response = client.post(
        '/users/',
        json={
            'username': 'string',
            'email': 'user@example.com',
            'password': 'string',
        },
    )
    assert response.status_code == HTTPStatus.CREATED
    assert response.json() == {
        'id': 1,
        'username': 'string',
        'email': 'user@example.com',
    }


def test_read_users(client):
    response = client.get('/users/')
    print(response.json())
    assert response.status_code == HTTPStatus.OK
    assert response.json() == [
            {
                'id': 1,
                'username': 'string',
                'email': 'user@example.com',
            }
        ]



def test_read_user(client):
    response = client.get('/users/1')
    assert response.status_code == HTTPStatus.OK


def test_read_user_not_found(client):
    response = client.get('/users/999')
    assert response.status_code == HTTPStatus.NOT_FOUND
    assert response.json() == {'detail': 'User not found'}


def test_update_user(client):
    response = client.put(
        '/users/1',
        json={
            'username': 'string',
            'email': 'user@example.com',
            'password': 'string',
        },
    )
    print(response.json())
    assert response.status_code == HTTPStatus.OK
    assert response.json() =={
        'id': 1,
        'username': 'string',
        'email': 'user@example.com',
    }
    

def test_delete_user(client):
    response = client.delete('/users/1')
    assert response.status_code == HTTPStatus.NO_CONTENT


def test_delete_user_not_found(client):
    response = client.delete('/users/999')
    assert response.status_code == HTTPStatus.NOT_FOUND
    assert response.json() == {'detail': 'User not found'}
