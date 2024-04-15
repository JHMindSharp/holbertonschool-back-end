#!/usr/bin/python3
"""
This module contains a script that fetches tasks for all employees using
the JSONPlaceholder API and exports them to a
JSON file formatted by employee ID.
"""

import json
import requests


def export_all_tasks():
    """
    Exports tasks for all employees to a JSON file.
    """
    users_url = 'https://jsonplaceholder.typicode.com/users'
    todos_url = 'https://jsonplaceholder.typicode.com/todos'

    users_response = requests.get(users_url)
    todos_response = requests.get(todos_url)

    if users_response.ok and todos_response.ok:
        users = users_response.json()
        todos = todos_response.json()

        user_tasks = {}
        for user in users:
            user_id = user['id']
            user_tasks[user_id] = [{
                'username': user['username'],
                'task': task['title'],
                'completed': task['completed']
            } for task in todos if task['userId'] == user_id]

        with open('todo_all_employees.json', 'w') as jsonfile:
            json.dump(user_tasks, jsonfile, indent=4)


if __name__ == "__main__":
    export_all_tasks()
