#!/usr/bin/python3
"""Gather data from an API"""
import csv
import requests
from sys import argv


if __name__ == "__main__":
    user_id = argv[1]
    url = "https://jsonplaceholder.typicode.com/"
    user = requests.get(url + "users/{}".format(user_id)).json()
    to_do = requests.get(url + "todos", params={"userId": user_id}).json()
    with open("{}.csv".format(user_id), "w") as csvfile:
        writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        [writer.writerow([user_id, user.get("username"),
                          task.get("completed"), task.get("title")])
         for task in to_do]
