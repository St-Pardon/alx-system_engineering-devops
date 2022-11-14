#!/usr/bin/python3
'''Script that fetch data from an API.
'''
import re
import requests
import sys


URL = 'https://jsonplaceholder.typicode.com'
'''The API's URL.'''


if __name__ == '__main__':
    if len(sys.argv) > 1:
        if re.fullmatch(r'\d+', sys.argv[1]):
            id = int(sys.argv[1])
            user_data = requests.get('{}/users/{}'.format(URL, id)).json()
            todo_data = requests.get('{}/todos'.format(URL)).json()
            user_name = user_data.get('name')
            todos = list(filter(lambda x: x.get('userId') == id, todo_data))
            todos_done = list(filter(lambda x: x.get('completed'), todos))
            print(
                'Employee {} is done with tasks({}/{}):'.format(
                    user_name,
                    len(todos_done),
                    len(todos)
                )
            )
            for todo_done in todos_done:
                print('\t {}'.format(todo_done.get('title')))
