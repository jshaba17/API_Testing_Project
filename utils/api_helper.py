import requests

BASE_URL = "https://jsonplaceholder.typicode.com"

def get_todos():
    """GET /todos endpoint."""
    response = requests.get(f"{BASE_URL}/todos")
    return response

def get_todo_by_id(todo_id):
    """GET /todos/{id} endpoint."""
    response = requests.get(f"{BASE_URL}/todos/{todo_id}")
    return response

def create_todo(data):
    """POST /todos endpoint."""
    response = requests.post(f"{BASE_URL}/todos", json=data)
    return response

def update_todo(todo_id, data):
    """PUT /todos/{id} endpoint."""
    response = requests.put(f"{BASE_URL}/todos/{todo_id}", json=data)
    return response

def delete_todo(todo_id):
    """DELETE /todos/{id} endpoint."""
    response = requests.delete(f"{BASE_URL}/todos/{todo_id}")
    return response
