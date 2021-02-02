#!/usr/bin/python3
"""
get data from an api based on the userd id that is passed as argument
"""
import json
import requests
from sys import argv


if __name__ == "__main__":

    if len(argv) == 2:
        url_base = 'https://jsonplaceholder.typicode.com/users/'
        person_url = '{}{}'.format(url_base, argv[1])
        todos_url = '{}{}/{}'.format(url_base, argv[1], 'todos')

        """ do two request
        one for user personal info and for todos tasks
        """
        person_res = requests.get(person_url)
        todos_res = requests.get(todos_url)

        """ get the obj responses body"""
        person_obj = person_res.json()
        todos_obj = todos_res.json()

        """ working with the data """
        filename = '{}.json'.format(person_obj['id'])
        username = person_obj['username']
        result = []

        for obj in todos_obj:
            task = {}
            task['task'] = obj['title']
            task['completed'] = obj['completed']
            task['username'] = username
            result.append(task)

        with open(filename, 'w') as f:
            json.dump({person_obj['id']: result}, f)
