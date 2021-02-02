#!/usr/bin/python3
"""
get data from an api based on the userd id that is passed as argument
"""

import csv
import json
import requests
from sys import argv


if __name__ == "__main__":

    url = 'https://jsonplaceholder.typicode.com/users/'
    todos = 'https://jsonplaceholder.typicode.com/todos/'

    person_obj = requests.get(url).json()
    res = requests.get(todos).json()

    """ working with the data """
    total = {}

    for user in person_obj:
        _id = user['id']
        result = []

        for obj in res:
            if _id == obj['userId']:
                task = {}
                task['task'] = obj['title']
                task['completed'] = obj['completed']
                task['username'] = user['username']
                result.append(task)
        total[_id] = result

    with open('todo_all_employees.json', 'w') as f:
        json.dump(total, f)
