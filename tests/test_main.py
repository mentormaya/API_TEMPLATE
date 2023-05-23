from fastapi.testclient import TestClient
from fastapi.responses import FileResponse
from app.main import api

client = TestClient(api)

def test_health_check():
    response = client.get("/healthcheck")
    assert response.status_code == 200
    assert response.json() == {"heartbeat": "I am alive!"}

# def test_get_favicon():
#     response = client.get("/favicon.ico")
#     assert response.status_code == 200
#     assert response == FileResponse