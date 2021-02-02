#!/usr/bin/python3
"""
get data from an api based on the userd id that is passed as argument
"""

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
        done_count = 0
        done_tasks = []

        for obj in todos_obj:
            if obj['completed'] is True:
                done_count += 1
                done_tasks.append(obj['title'])

        st = 'Employee {} is done with tasks({}/{}):'
        print(st.format(person_obj['name'], done_count, len(todos_obj)))
        for task in done_tasks:
            print('\t {}'.format(task))
