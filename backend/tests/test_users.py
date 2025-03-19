import pytest

from backend.main import app
from backend.models import db


@pytest.fixture
def client():
    """ Creates a Flask test client """
    return app.test_client()

@pytest.fixture
def reset_database():
    """ Clearing the database before each test """
    with app.app_context():
        db.drop_all()
        db.create_all()


def test_create_user_missing_name(client):
    response = client.post('/users', json={'email': 'admin@gmail.com'})
    assert response.status_code == 400
    data = response.get_json()
    assert data['error'] == 'Name and email required'
    

def test_create_user_missing_email(client):
    response = client.post('/users', json={'name': 'admin'})
    assert response.status_code == 400
    data = response.get_json()
    assert data['error'] == 'Name and email required'
    
    
def test_create_user_user_exists(client):
    client.post('/users', json={'name': 'test_user', 'email': 'test_user@gmail.com'})
    response = client.post('/users', json={'name': 'test_user', 'email': 'test_user@gmail.com'})
    assert response.status_code == 400
    data = response.get_json()
    assert data['error'] == 'User already exists'
    

def test_get_all_users(client):
    response = client.get('/users')
    assert response.status_code == 200


def test_get_user_by_id(client):
    response = client.get('/users/88888888888888')
    assert response.status_code == 404
    data = response.get_json()
    assert data['error'] == 'User not found'


def test_update_user_missing_name(client):
    response = client.put('/users/1', json={'email': 'test_user@gmail.com'})
    assert response.status_code == 400
    data = response.get_json()
    assert data['error'] == 'Name and email required'


def test_update_user_missing_email(client):
    response = client.put('/users/1', json={'name': 'test_user'})
    assert response.status_code == 400
    data = response.get_json()
    assert data['error'] == 'Name and email required'
    

def test_update_user_user_not_found(client):
    response = client.put('/users/888888888888888', json={'email': 'test_user1@gmail.com', 'name': 'test_user_1'})
    assert response.status_code == 404
    data = response.get_json()
    assert data['error'] == 'User not found'


def test_delete_user_user_not_found(client):
    response = client.delete('/users/888888888888888')
    assert response.status_code == 404
    data = response.get_json()
    assert data['error'] == 'User not found'
    

def test_delete_user_ok(client):
    response = client.post('/users', json={'name': 'test_user3333', 'email': 'test_user3333@gmail.com'})
    data = response.get_json()
    user_id = data['user_id']
    response = client.delete(f'users/{user_id}')
    assert response.status_code == 200