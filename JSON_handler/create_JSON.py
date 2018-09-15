"""
Initialise a new data.json file
"""
import json


def create_json():
    data = data = dict(watched=[], pending=[])
    with open("data.json", "w") as fileopen:
        json.dump(data, fileopen)