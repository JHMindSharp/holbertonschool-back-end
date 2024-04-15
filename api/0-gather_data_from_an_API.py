#!/usr/bin/python3
import requests
import sys

def fetch_todo_list(employee_id):
    """Fetches the TODO list for a given employee ID using JSONPlaceholder API."""
    user_url = f'https://jsonplaceholder.typicode.com/users/{employee_id}'
    todos_url = f'https://jsonplaceholder.typicode.com/todos?userId={employee_id}'

    user_response = requests.get(user_url)
    todos_response = requests.get(todos_url)

    if user_response.ok and todos_response.ok:
        user = user_response.json()
        todos = todos_response.json()

        completed_tasks = [task for task in todos if task['completed']]
        total_tasks = todos

        print(f"Employee {user['name']} is done with tasks({len(completed_tasks)}/{len(total_tasks)}):")
        for task in completed_tasks:
            print(f"\t {task['title']}")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        fetch_todo_list(sys.argv[1])

