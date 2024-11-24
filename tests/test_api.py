import unittest
import requests

# Define your helper functions or API interaction functions here
def get_todos():
    """GET /todos endpoint."""
    return requests.get("https://jsonplaceholder.typicode.com/todos")

def get_todo_by_id(todo_id):
    """GET /todos/{id} endpoint."""
    return requests.get(f"https://jsonplaceholder.typicode.com/todos/{todo_id}")

def create_todo(data):
    """POST /todos endpoint."""
    return requests.post("https://jsonplaceholder.typicode.com/todos", json=data)

def update_todo(todo_id, data):
    """PUT /todos/{id} endpoint."""
    return requests.put(f"https://jsonplaceholder.typicode.com/todos/{todo_id}", json=data)

def delete_todo(todo_id):
    """DELETE /todos/{id} endpoint."""
    return requests.delete(f"https://jsonplaceholder.typicode.com/todos/{todo_id}")


# Define your test cases
class TestAPI(unittest.TestCase):

    def test_get_todos(self):
        response = get_todos()
        self.assertEqual(response.status_code, 200)
        self.assertTrue(len(response.json()) > 0)  # Ensures there are some todos

    def test_get_todo_by_id(self):
        response = get_todo_by_id(1)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['id'], 1)  # Ensure the returned todo has ID = 1

    def test_create_todo(self):
        new_todo = {
            "title": "New Todo",
            "completed": False,
            "userId": 1
        }
        response = create_todo(new_todo)
        self.assertEqual(response.status_code, 201)  # Status 201 for created resource
        self.assertEqual(response.json()['title'], new_todo['title'])

    def test_update_todo(self):
        updated_todo = {
            "title": "Updated Todo",
            "completed": True,
            "userId": 1
        }
        response = update_todo(1, updated_todo)  # Update todo with ID 1
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['title'], updated_todo['title'])

    def test_delete_todo(self):
        response = delete_todo(1)  # Delete todo with ID 1
        self.assertEqual(response.status_code, 200)

        # Verify the todo is deleted by trying to fetch it again
        response = get_todo_by_id(1)
        self.assertEqual(response.status_code, 404)  # Ensure it returns a 404 error

if __name__ == '__main__':
    unittest.main()
