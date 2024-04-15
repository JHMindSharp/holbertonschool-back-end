#!/usr/bin/python3
"""
This module fetches the TODO list for a given employee from JSONPlaceholder API
and displays their progress.
"""

import requests
import sys


def fetch_todo_list(employee_id):
    """
    Fetches the TODO list for a given employee ID using JSONPlaceholder API
    and prints the progress.

    Args:
        employee_id (int): The ID of the employee to query.
    """
    try:
        employee_id = int(employee_id)  # Convert employee ID to integer
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

        completed_tasks = [task for task in todos if task.get('completed')]
        total_tasks = len(todos)

        print(f"Employee {user.get('name', 'Unknown')} is done with tasks"
              f"({len(completed_tasks)}/{total_tasks}):")
        for task in completed_tasks:
            print(f"\t {task.get('title')}")


if __name__ == "__main__":
    if len(sys.argv) > 1:
        fetch_todo_list(sys.argv[1])
