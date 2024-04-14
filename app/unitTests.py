import pytest
from flask.testing import FlaskClient
from app import app  # Import the Flask app instance directly
from mongomock import MongoClient
from unittest.mock import patch
from pymongo.errors import DuplicateKeyError
from bson.objectid import ObjectId


@pytest.fixture
def client():
    app.config['TESTING'] = True
    # Replace the Mongo client with a mongomock client
    with patch('app.mongo', MongoClient()):
        with app.test_client() as client:
            yield client

def test_get_top_documents(client: FlaskClient):
    # Assuming mongomock is properly mocking data
    response = client.get('/leaderboard/top')
    assert response.status_code == 200
    assert isinstance(response.json, list)  # assuming it should return a list

def test_get_all_documents_asc(client: FlaskClient):
    response = client.get('/leaderboard/all')
    assert response.status_code == 200
    assert isinstance(response.json, list)

def test_create_document(client: FlaskClient):
    # Make sure each test uses unique data or reset the mock database
    valid_username = str(ObjectId())
    unique_user = {"username": valid_username, "score": 100}
    response = client.post('/create', json=unique_user)
    assert response.status_code == 201, "Expected document to be created successfully"

    unique_user = {"username": valid_username, "score": 1880}
    response = client.post('/create', json=unique_user)
    assert response.status_code == 409
    assert response.json == {"error": "A document with the same username already exists."}

def test_update_document_no_change(client: FlaskClient):
    # Create a realistic ObjectId
    valid_id = str(ObjectId())
    response = client.put(f'/update/{valid_id}', json={"score": 67})  # Assuming score was already 67
    assert response.status_code == 200
    assert response.json == {"error": "Document not found or no update was necessary"}

def test_update_document_not_found(client: FlaskClient):
    # Generate an ObjectId for an assumed non-existent document
    non_existent_id = str(ObjectId())
    response = client.put(f'/update/{non_existent_id}', json={"score": 67})
    assert response.status_code == 200
    assert response.json == {"error": "Document not found or no update was necessary"}

