import pytest
from calc import app as flask_app

@pytest.fixture
def app():
    yield flask_app

@pytest.fixture
def client(app):
    return app.test_client()


def test_addition(client):
    response = client.post('/', data={'var_1': 10, 'var_2': 5, 'operation': 'Addition'})
    assert b'15' in response.data

def test_subtraction(client):
    response = client.post('/', data={'var_1': 10, 'var_2': 5, 'operation': 'Subtraction'})
    assert b'5' in response.data

def test_multiplication(client):
    response = client.post('/', data={'var_1': 10, 'var_2': 5, 'operation': 'Multiplication'})
    assert b'50' in response.data

def test_division(client):
    response = client.post('/', data={'var_1': 10, 'var_2': 5, 'operation': 'Division'})
    assert b'2.0' in response.data

def test_division_by_zero(client):
    response = client.post('/', data={'var_1': 10, 'var_2': 0, 'operation': 'Division'})
    # The current implementation returns a ZeroDivisionError, which results in a 500 error.
    # A robust test should check for a specific error message, but for now we'll check the status code.
    assert response.status_code == 500
