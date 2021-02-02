#!/usr/bin/python3
"""
get data from an api based on the userd id that is passed as argument
"""

import csv
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
        name = person_obj['username']
        filename = '{}.csv'.format(person_obj['id'])

        with open(filename, 'w', newline='') as f:
            for obj in todos_obj:
                line = [obj['userId'], name, obj['completed'], obj['title']]
                writer = csv.writer(f, delimiter=',', quotechar='"',
                                    quoting=csv.QUOTE_ALL)
                writer.writerow(line)
