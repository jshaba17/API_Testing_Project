import requests

BASE_URL = "https://jsonplaceholder.typicode.com"

def get_todos():
    response = requests.get(f"{BASE_URL}/todos")
    return response

def get_todo_by_id(todo_id):
    response = requests.get(f"{BASE_URL}/todos/{todo_id}")
    return response

def create_todo(data):
    response = requests.post(f"{BASE_URL}/todos", json=data)
    return response

def update_todo(todo_id, data):
    response = requests.put(f"{BASE_URL}/todos/{todo_id}", json=data)
    return response

def delete_todo(todo_id):
    response = requests.delete(f"{BASE_URL}/todos/{todo_id}")
    return response
