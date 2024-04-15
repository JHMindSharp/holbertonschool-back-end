#!/usr/bin/python3
"""
This module contains a script that uses the JSONPlaceholder API to fetch tasks
for a given employee and exports them to a CSV file.
"""

import csv
import requests
import sys


def export_to_csv(employee_id):
    """
    Exports tasks for a given employee ID to a CSV file.

    Args:
        employee_id (int): The employee ID for which to fetch tasks.
    """
    try:
        employee_id = int(employee_id)
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

        with open(f'{employee_id}.csv', 'w', newline='') as csvfile:
            fieldnames = ['USER_ID', 'USERNAME',
                          'TASK_COMPLETED_STATUS', 'TASK_TITLE']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames,
                                    quoting=csv.QUOTE_ALL)

            for task in todos:
                writer.writerow({
                    'USER_ID': employee_id,
                    'USERNAME': user.get('username'),
                    'TASK_COMPLETED_STATUS': task.get('completed'),
                    'TASK_TITLE': task.get('title')
                })


if __name__ == "__main__":
    if len(sys.argv) > 1:
        export_to_csv(sys.argv[1])
