import pytest
from app import app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_home(client):
    response = client.get("/")
    assert response.status_code == 200
    assert b"Welcome to Render CI/CD Pipeline!" in response.data

def test_about(client):
    response = client.get("/about")
    assert response.status_code == 200
    assert b"This is a Flask application" in response.data

def test_health(client):
    response = client.get("/health")
    assert response.status_code == 200
    assert response.get_json() == {"status": "healthy", "message": "The application is running fine."}

def test_api_data(client):
    response = client.get("/api/data")
    assert response.status_code == 200
    assert response.get_json() == {
        "id": 1,
        "name": "Render CI/CD Example",
        "description": "This endpoint returns sample data in JSON format."
    }
