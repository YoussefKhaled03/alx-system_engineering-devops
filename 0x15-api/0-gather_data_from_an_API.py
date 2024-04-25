#!/usr/bin/python3

'''
A script that, using this REST API, for a given employee ID, returns information about his/her TODO list progress.
'''

from requests import get
from sys import argv

if __name__ == "__main__":
    main_url = "https://jsonplaceholder.typicode.com"
    todo_link = main_url + "/users/{}/todos".format(argv[1])
    user_link = main_url + "/users/{}".format(argv[1])
    todo_response = get(todo_link).json()
    user_response = get(user_link).json()

    total_tasks = len(todo_response)
    done_tasks = len([task for task in todo_response if task.get("completed")])

    name = user_response.get("name")
    print("Employee {} is done with tasks({}/{}):".format(name, done_tasks, total_tasks))
    for task in todo_response:
        if task.get("completed"):
            print("\t {}".format(task.get("title")))
