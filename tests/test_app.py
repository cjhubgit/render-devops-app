import sys
import os
import pytest

# Ensure the project root is in the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from app import app  # Import the Flask app

@pytest.fixture
def client():
    with app.test_client() as client: 
        yield client  # Create a test client for the app

def test_home(client):
    response = client.get("/")  # Simulate a GET request to the home route
    assert response.status_code == 200  # Check that the response status code is 200 (OK)
    assert b"Welcome to Render CI/CD Pipeline!" in response.data  # Check that the response contains the welcome message

def test_feedback_get(client):
    response = client.get("/feedback")  # Simulate a GET request to the feedback route
    assert response.status_code == 200  # Check that the response status code is 200 (OK)
    assert b"Enter your feedback:" in response.data  # Check that the response contains the feedback form