"""
Read data from data.json
"""
import json
import os.path

def get_data():
    # check if data.json file exists
    if os.path.isfile("data.json"):
        with open('data.json', 'r') as fileopen:
            data = json.load(fileopen)
        return data
    else:
        print("Data does not exist, unable to return data")