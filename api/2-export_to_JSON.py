#!/usr/bin/python3
"""
This module contains a script that fetches tasks for a given employee using
the JSONPlaceholder API and exports them to a JSON file
formatted by employee ID.
"""

import json
import requests
import sys


def export_to_json(employee_id):
    """
    Exports tasks for a given employee ID to a JSON file.

    Args:
        employee_id (int): The employee ID for which to fetch tasks.
    """
    try:
        employee_id = int(employee_id)  # Convert input to integer
    except ValueError:
        print("Error: Employee ID must be an integer.")
        return

    user_url = (
        f'https://jsonplaceholder.typicode.com/users/{employee_id}')
    todos_url = (
        f'https://jsonplaceholder.typicode.com/todos?userId={employee_id}')

    user_response = requests.get(user_url)
    todos_response = requests.get(todos_url)

    if user_response.ok and todos_response.ok:
        user = user_response.json()
        todos = todos_response.json()

        tasks = [{
            'username': user.get('username'),
            'task': task.get('title'),
            'completed': task.get('completed')
        } for task in todos]

        with open(f'{employee_id}.json', 'w') as jsonfile:
            json.dump({str(employee_id): tasks}, jsonfile, indent=4)


if __name__ == "__main__":
    if len(sys.argv) > 1:
        export_to_json(sys.argv[1])
