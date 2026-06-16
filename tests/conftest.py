import pytest
from fastapi.testclient import TestClient

from tabacaria_pj.app import app


@pytest.fixture
def client():
    return TestClient(app)
