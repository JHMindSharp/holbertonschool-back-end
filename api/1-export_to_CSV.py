#!/usr/bin/python3
import csv
import requests
import sys


def export_to_csv(employee_id):
    """Exports employee tasks to a CSV file using JSONPlaceholder API."""
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
            task_writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
            for task in todos:
                task_writer.writerow([employee_id, user['username'],
                                      task['completed'], task['title']])


if __name__ == "__main__":
    if len(sys.argv) > 1:
        export_to_csv(sys.argv[1])
