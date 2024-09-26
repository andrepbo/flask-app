import pytest
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_get_all_tasks(client):
    response = client.get('/tasks')
    assert response.status_code == 200
    assert len(response.json) == 2

def test_get_task_by_id(client):
    response = client.get('/tasks/1')
    assert response.status_code == 200
    assert response.json["title"] == "Learn Flask"

def test_create_task(client):
    new_task = {"title": "New Task", "description": "Task for testing"}
    response = client.post('/tasks', json=new_task)
    assert response.status_code == 201
    assert response.json["title"] == "New Task"

def test_update_task(client):
    updated_task = {"title": "Updated Task", "description": "Updated description"}
    response = client.put('/tasks/1', json=updated_task)
    assert response.status_code == 200
    assert response.json["title"] == "Updated Task"

def test_delete_task(client):
    response = client.delete('/tasks/1')
    assert response.status_code == 204
    # Ensure task is deleted
    response = client.get('/tasks/1')
    assert response.status_code == 404