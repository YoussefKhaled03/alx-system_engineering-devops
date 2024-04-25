#!/usr/bin/python3

'''
A script that, using this REST API, for a given employee ID, returns information about his/her TODO list progress then exports to JSON.
'''

from json import dump
from requests import get
from sys import argv

if __name__ == "__main__":
    main_url = "https://jsonplaceholder.typicode.com"
    todo_link = main_url + "/users/{}/todos".format(argv[1])
    user_link = main_url + "/users/{}".format(argv[1])
    todo_response = get(todo_link).json()
    user_response = get(user_link).json()

    todo_list = []
    for task in todo_response:
        task_dict = {}
        task_dict.update({"task": task.get("title"), "completed": task.get("completed"), "username": user_response.get("username")})
        todo_list.append(task_dict)

    with open("{}.json".format(argv[1]), "w") as json_file:
        dump({argv[1]: todo_list}, json_file)
