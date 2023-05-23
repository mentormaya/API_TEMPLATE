from fastapi.testclient import TestClient
from app.main import api

client = TestClient(api)

def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"msg": "Hello World"}

def test_get_favicon():
    response = client.get("/favicon.ico")
    assert response.status_code == 200
    assert response.json() == {"msg": "no favicon needed"}