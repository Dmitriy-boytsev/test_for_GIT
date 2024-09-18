import pytest
from fastapi.testclient import TestClient
from app import app

client = TestClient(app)

def test_get_user_info_success():
    response = client.get("/api/users/1")
    assert response.status_code == 200
    assert "username" in response.json()
    assert "email" in response.json()

def test_get_user_info_not_found():
    response = client.get("/api/users/9999")
    assert response.status_code == 404
    assert response.json() == {"detail": "User not found"}

def test_invalid_user_id():
    response = client.get("/api/users/abc")
    assert response.status_code == 422
