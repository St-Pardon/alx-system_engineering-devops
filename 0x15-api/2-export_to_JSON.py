#!/usr/bin/python3
'''Script that fetchs data from an API and exports it to a JSON file.
'''
import json
import re
import requests
import sys


API = 'https://jsonplaceholder.typicode.com'
'''The API's URL.'''


if __name__ == '__main__':
    if len(sys.argv) > 1:
        if re.fullmatch(r'\d+', sys.argv[1]):
            id = int(sys.argv[1])
            user_data = requests.get('{}/users/{}'.format(API, id)).json()
            todos_data = requests.get('{}/todos'.format(API)).json()
            user_name = user_data.get('username')
            todos = list(filter(lambda x: x.get('userId') == id, todos_data))
            with open('{}.json'.format(id), 'w') as file:
                data = list(map(
                    lambda x: {
                        'task': x.get('title'),
                        'completed': x.get('completed'),
                        'username': user_name
                    },
                    todos
                ))
                data = {
                    '{}'.format(id): data
                }
                json.dump(data, file)
