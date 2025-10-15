# file: tests/test_api.py
import pytest
from httpx import AsyncClient
from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)

@pytest.fixture(scope="module")
def anyio_backend():
    return "asyncio"

@pytest.mark.anyio
async def test_create_todo():
    response = client.post("/todos/", json={"title": "Test Todo", "completed": False})
    assert response.status_code == 200
    data = response.json()
    assert data["title"] == "Test Todo"
    assert data["completed"] == False
    assert "id" in data

@pytest.mark.anyio
async def test_read_todos():
    response = client.get("/todos/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

@pytest.mark.anyio
async def test_read_todo():
    response = client.post("/todos/", json={"title": "Read Me", "completed": False})
    todo_id = response.json()["id"]
    response = client.get(f"/todos/{todo_id}")
    assert response.status_code == 200
    data = response.json()
    assert data["title"] == "Read Me"
    assert data["id"] == todo_id

@pytest.mark.anyio
async def test_update_todo():
    response = client.post("/todos/", json={"title": "Update Me", "completed": False})
    todo_id = response.json()["id"]
    response = client.patch(f"/todos/{todo_id}", json={"title": "Updated Title", "completed": True})
    assert response.status_code == 200
    data = response.json()
    assert data["title"] == "Updated Title"
    assert data["completed"] == True

@pytest.mark.anyio
async def test_delete_todo():
    response = client.post("/todos/", json={"title": "Delete Me", "completed": False})
    todo_id = response.json()["id"]
    response = client.delete(f"/todos/{todo_id}")
    assert response.status_code == 200
    response = client.get(f"/todos/{todo_id}")
    assert response.status_code == 404
