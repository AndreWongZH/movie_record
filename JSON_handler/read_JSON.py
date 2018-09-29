"""
Read data from data.json
"""
import json
import os.path

def get_data():
    # check if data.json file exists
    if os.path.isfile("A:\Coding projects\main projects folder\movie_record\JSON_handler\data.json"):
        with open('A:\Coding projects\main projects folder\movie_record\JSON_handler\data.json', 'r') as fileopen:
            data = json.load(fileopen)
        return data
    else:
        print("Data does not exist, unable to return data")

