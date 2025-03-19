import pytest

from backend.main import app
from backend.models import db
from backend.utils import is_valid_email


@pytest.fixture
def client():
    """
        Creates a Flask test client
        to send requests in tests.
    """
    return app.test_client()


@pytest.fixture
def reset_database():
    """
        Clears the database before each test.
    """
    with app.app_context():
        db.drop_all()
        db.create_all()


def test_create_user_missing_name(client):
    """
        Tests creating a user without a name.
        Expects a 400 error with the message 'Name and email required'.
    """
    response = client.post('/users', json={'email': 'admin@gmail.com'})
    assert response.status_code == 400
    data = response.get_json()
    assert data['error'] == 'Name and email required'


def test_create_user_missing_email(client):
    """
        Tests creating a user without an email.
        Expects a 400 error with the message 'Name and email required'.
    """
    response = client.post('/users', json={'name': 'admin'})
    assert response.status_code == 400
    data = response.get_json()
    assert data['error'] == 'Name and email required'
    

def test_create_user_invalid_email(client):
    """
        Tests creating a user with invalid email.
        Expects a 400 error with the message 'Invalid email format'.
    """
    response = client.post('/users', json={'name': 'admin123456789', 'email': 'admin123456789'})
    assert response.status_code == 400
    data = response.get_json()
    assert data['error'] == 'Invalid email format'
    


def test_create_user_user_exists(client):
    """
        Tests creating a user that already exists. 
        Expects a 400 error with the message 'User already exists'.
    """
    client.post('/users', json={'name': 'test_user', 'email': 'test_user@gmail.com'})
    response = client.post('/users', json={'name': 'test_user', 'email': 'test_user@gmail.com'})
    assert response.status_code == 400
    data = response.get_json()
    assert data['error'] == 'User already exists'


def test_get_all_users(client):
    """
        Tests fetching all users.
        Expects a 200 status code.
    """
    response = client.get('/users')
    assert response.status_code == 200


def test_get_user_by_id(client):
    """
        Tests fetching a user by ID.
        Expects a 404 error with the message
        'User not found' for a non-existent user.
    """
    response = client.get('/users/88888888888888')
    assert response.status_code == 404
    data = response.get_json()
    assert data['error'] == 'User not found'


def test_update_user_missing_name(client):
    """
        Tests updating a user without a name.
        Expects a 400 error with the message 'Name and email required'.
    """
    response = client.put('/users/1', json={'email': 'test_user@gmail.com'})
    assert response.status_code == 400
    data = response.get_json()
    assert data['error'] == 'Name and email required'


def test_update_user_missing_email(client):
    """
        Tests updating a user without an email.
        Expects a 400 error with the message 'Name and email required'.
    """
    response = client.put('/users/1', json={'name': 'test_user'})
    assert response.status_code == 400
    data = response.get_json()
    assert data['error'] == 'Name and email required'
    

def test_update_user_invalid_email(client):
    """
        Tests updating a user with invalid email.
        Expects a 400 error with the message 'Invalid email format'.
    """
    response = client.put('/users/1', json={'name': 'test_user_123333', 'email': 'test_user_123333'})
    assert response.status_code == 400
    data = response.get_json()
    assert data['error'] == 'Invalid email format'
    


def test_update_user_user_not_found(client):
    """
        Tests updating a non-existent user.
        Expects a 404 error with the message 'User not found'.
    """
    response = client.put('/users/888888888888888', json={'email': 'test_user1@gmail.com', 'name': 'test_user_1'})
    assert response.status_code == 404
    data = response.get_json()
    assert data['error'] == 'User not found'


def test_delete_user_user_not_found(client):
    """
        Tests deleting a non-existent user.
        Expects a 404 error with the message 'User not found'.
    """
    response = client.delete('/users/888888888888888')
    assert response.status_code == 404
    data = response.get_json()
    assert data['error'] == 'User not found'


def test_delete_user_ok(client):
    """
        Tests deleting an existing user.
        Expects a 200 status code.
    """
    response = client.post('/users', json={'name': 'test_user3333', 'email': 'test_user3333@gmail.com'})
    data = response.get_json()
    user_id = data['user_id']
    response = client.delete(f'users/{user_id}')
    assert response.status_code == 200
