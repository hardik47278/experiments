import pytest
from fastapi.testclient import TestClient
from api.main import app   # 👈 imports your FastAPI app

client = TestClient(app)   # 👈 creates a test client (simulates requests to your API)

def test_home():
    response = client.get("/")    # 👈 calls the "/" endpoint
    assert response.status_code == 200   # 👈 ensures it returns HTTP 200 OK
    assert "Documental portal" in response.text  # 👈 checks if response body contains this string
