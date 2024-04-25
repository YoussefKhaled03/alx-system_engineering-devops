#!/usr/bin/python3
"""
A script that, using this REST API, for a given employee ID, returns information about his/her TODO list progress then exports to CSV.
"""

from csv import DictWriter, QUOTE_ALL
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
        task_dict.update({"user_ID": argv[1], "username": user_response.get(
            "username"), "completed": task.get("completed"),
                          "task": task.get("title")})
        todo_list.append(task_dict)

    with open("{}.csv".format(argv[1]), "w") as csv_file:
        csv_writer = DictWriter(csv_file, fieldnames=[
                                "user_ID", "username", "completed", "task"], quoting=QUOTE_ALL)
        csv_writer.writeheader()
        csv_writer.writerows(todo_list)
