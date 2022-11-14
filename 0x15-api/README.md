# 0x15. API

## Requirements
- Allowed editors: `vi`, `vim`, `emacs`
- All your files will be interpreted/compiled on Ubuntu 14.04 LTS using `python3` (version 3.4.3)
- All your files should end with a new line
- The first line of all your files should be exactly `#!/usr/bin/python3`
- **Libraries imported in your Python files must be organized in alphabetical order**
- A `README.md` file, at the root of the folder of the project, is mandatory
- Your code should use the `PEP 8` style
- All your files must be executable
- The length of your files will be tested using `wc`
- All your modules should have a documentation (`python3 -c 'print(__import__("my_module").__doc__)'`)
- You must use [get](https://docs.python.org/3.4/library/stdtypes.html#dict.get) to access to dictionary value by key (it won’t throw an exception if the key doesn’t exist in the dictionary)
- Your code should not be executed when imported (by using if `__name__ == "__main__":`)


## Tasks
### [0. Gather data from an API](./0-gather_data_from_an_API.py)
Write a Python script that, using this [REST API](https://jsonplaceholder.typicode.com/), for a given employee ID, returns information about his/her TODO list progress.

**Requirements:**

- [x] You must use `urllib` or `requests` module
- [x] The script must accept an integer as a parameter, which is the employee ID
- [x] The script must display on the standard output the employee TODO list progress in this exact format:
  - [x] First line: `Employee EMPLOYEE_NAME is done with tasks(NUMBER_OF_DONE_TASKS/TOTAL_NUMBER_OF_TASKS):`
    - [x] `EMPLOYEE_NAME`: name of the employee
    - [x] `NUMBER_OF_DONE_TASKS`: number of completed tasks
    - [x] `TOTAL_NUMBER_OF_TASKS`: total number of tasks, which is the sum of completed and non-completed tasks
  - [x] Second and N next lines display the title of completed tasks: `TASK_TITLE` (with 1 tabulation and 1 space before the `TASK_TITLE`)

### [1. Export to CSV](./1-export_to_CSV.py)

Using what you did in the task #0, extend your Python script to export data in the CSV format.

**Requirements:**

- [x] Records all tasks that are owned by this employee
- [x] Format must be: `"USER_ID","USERNAME","TASK_COMPLETED_STATUS","TASK_TITLE"`
- [x] File name must be: `USER_ID.csv`


### [2. Export to JSON](./2-export_to_JSON.py)
Using what you did in the task #0, extend your Python script to export data in the JSON format.

**Requirements:**

- [x] Records all tasks that are owned by this employee
- [x] Format must be: `{ "USER_ID": [{"task": "TASK_TITLE", "completed": TASK_COMPLETED_STATUS, "username": "USERNAME"}, {"task": "TASK_TITLE", "completed": TASK_COMPLETED_STATUS, "username": "USERNAME"}, ... ]}`
- [x] File name must be: `USER_ID.json`

### [3. Dictionary of list of dictionaries](./3-dictionary_of_list_of_dictionaries.py)
Using what you did in the task #0, extend your Python script to export data in the JSON format.

Requirements:

- [x] Records all tasks from all employees
- [x] Format must be: `{ "USER_ID": [ {"username": "USERNAME", "task": "TASK_TITLE", "completed": TASK_COMPLETED_STATUS}, {"username": "USERNAME", "task": "TASK_TITLE", "completed": TASK_COMPLETED_STATUS}, ... ], "USER_ID": [ {"username": "USERNAME", "task": "TASK_TITLE", "completed": TASK_COMPLETED_STATUS}, {"username": "USERNAME", "task": "TASK_TITLE", "completed": TASK_COMPLETED_STATUS}, ... ]}`
- [x] File name must be: `todo_all_employees.json`
