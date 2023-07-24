#!/usr/bin/python3
"""Gather data from an API"""
import requests
from sys import argv


if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    user_id = argv[1]
    user = requests.get(url + "users/{}".format(user_id)).json()
    to_do = requests.get(url + "todos", params={"userId": user_id}).json()
    completed_tasks = [task for task in to_do if task.get("completed") is True]
    print("Employee {} is done with tasks({}/{}):".format(
        user.get("name"), len(completed_tasks), len(to_do)))
    [print("\t{}".format(task.get("title"))) for task in completed_tasks]
