from http import HTTPStatus

from fastapi.testclient import TestClient

from tabacaria_pj.app import app

client = TestClient(app)


def test_ola():
    client = TestClient(app)

    response = client.get('/')
    assert response.json() == {'message': 'ola mundo'}
    assert response.status_code == HTTPStatus.OK
