#!/usr/bin/python3
import json
import requests
import sys


def export_to_json(employee_id):
    """Exports employee tasks to a JSON file using JSONPlaceholder API."""
    user_url = (
        f'https://jsonplaceholder.typicode.com/users/{employee_id}')
    todos_url = (
        f'https://jsonplaceholder.typicode.com/todos?userId={employee_id}')

    user_response = requests.get(user_url)
    todos_response = requests.get(todos_url)

    if user_response.ok and todos_response.ok:
        user = user_response.json()
        todos = todos_response.json()

        tasks = [{"task": task['title'],
                  "completed": task['completed'], "username": user['username']}
                 for task in todos]

        tasks_dict = {employee_id: tasks}

        with open(f'{employee_id}.json', 'w') as jsonfile:
            json.dump(tasks_dict, jsonfile, indent=4)


if __name__ == "__main__":
    if len(sys.argv) > 1:
        export_to_json(sys.argv[1])
