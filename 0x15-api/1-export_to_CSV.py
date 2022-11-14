#!/usr/bin/python3
'''Script to fetch data and export data from an API to a CSV file.
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
            todos_data = requests.get('{}/todos'.format(URL)).json()
            user_name = user_data.get('username')
            todos = list(filter(lambda x: x.get('userId') == id, todos_data))
            with open('{}.csv'.format(id), 'w') as file:
                for todo in todos:
                    file.write(
                        '"{}","{}","{}","{}"\n'.format(
                            id,
                            user_name,
                            todo.get('completed'),
                            todo.get('title')
                        )
                    )
