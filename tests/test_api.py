import unittest
import requests


def get_todos():
    
    return requests.get("https://jsonplaceholder.typicode.com/todos")

def get_todo_by_id(todo_id):
    
    return requests.get(f"https://jsonplaceholder.typicode.com/todos/{todo_id}")

def create_todo(data):
    "POST /todos endpoint."
    return requests.post("https://jsonplaceholder.typicode.com/todos", json=data)

def update_todo(todo_id, data):
    "PUT /todos/{id} endpoint."
    return requests.put(f"https://jsonplaceholder.typicode.com/todos/{todo_id}", json=data)

def delete_todo(todo_id):
    "DELETE /todos/{id} endpoint."
    return requests.delete(f"https://jsonplaceholder.typicode.com/todos/{todo_id}")


class TestAPI(unittest.TestCase):

    def test_get_todos(self):
        response = get_todos()
        self.assertEqual(response.status_code, 200)
        self.assertTrue(len(response.json()) > 0)  

    def test_get_todo_by_id(self):
        response = get_todo_by_id(1)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['id'], 1)  

    def test_create_todo(self):
        new_todo = {
            "title": "New Todo",
            "completed": False,
            "userId": 1
        }
        response = create_todo(new_todo)
        self.assertEqual(response.status_code, 201)  
        self.assertEqual(response.json()['title'], new_todo['title'])

    def test_update_todo(self):
        updated_todo = {
            "title": "Updated Todo",
            "completed": True,
            "userId": 1
        }
        response = update_todo(1, updated_todo)  
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['title'], updated_todo['title'])

    def test_delete_todo(self):
        response = delete_todo(1)  
        self.assertEqual(response.status_code, 200)

      
        response = get_todo_by_id(1)
        self.assertEqual(response.status_code, 404)  

if __name__ == '__main__':
    unittest.main()
