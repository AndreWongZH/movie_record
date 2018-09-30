"""
Initialise a new data.json file
"""
import json


def create_json():
    data = data = dict(watched=[], pending=[])
    with open("A:\Coding projects\main projects folder\movie_record\JSON_handler\data.json", "w") as fileopen:
        json.dump(data, fileopen)