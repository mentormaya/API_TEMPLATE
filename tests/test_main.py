import httpx
import pytest
import logging
from app.main import api
from fastapi import status
from httpx import AsyncClient
from typing import AsyncIterator
from utils.constants import config
from fastapi.testclient import TestClient
from fastapi.responses import FileResponse

logger = logging.getLogger(__name__)

@pytest.fixture
def anyio_backend() -> str:
    return "asyncio"

@pytest.fixture()
async def ac() -> AsyncIterator[httpx.AsyncClient]:
    async with httpx.AsyncClient(app=api, base_url="http://testserver") as ac:
        yield ac

client = TestClient(api)

def test_read_main():
    response = client.get("/")
    app_info = {
        "title": config["APP_NAME"],
        "description": config["APP_DESCRIPTION"],
        "termsOfService": config["TERMS_OF_SERVICES"],
        "contact": {
            "name": config["APP_DEVELOPER"],
            "url": config["APP_DEV_WEB"],
            "email": config["APP_DEV_EMAIL"],
        },
        "license": {
            "name": config["APP_LICENSE_NAME"],
            "url": config["APP_LICENSE_URL"],
        },
        "version": config["APP_VERSION"],
    }
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == app_info

def test_health_check():
    response = client.get("/healthcheck")
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == {"heartbeat": "I am alive!"}

@pytest.mark.anyio
async def test_get_favicon():
    async with AsyncClient(app=api, base_url="http://test") as ac:
        response = await ac.get("/favicon.ico")
    assert response.status_code == status.HTTP_200_OK
    # assert type(response) == FileResponse