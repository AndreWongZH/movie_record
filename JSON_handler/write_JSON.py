"""
Format to write_data:
write_data(watched: True or False, Movie_Title)
"""
import json
from JSON_handler.read_JSON import get_data

def open_write(data):
    with open("A:\Coding projects\main projects folder\movie_record\JSON_handler\data.json", "w") as fileopen:
        json.dump(data, fileopen)

def write_data(watched, name):
    # this ensures that there is a data.json file
    data = get_data()

    if type(watched) != bool:
        print("Please state either True or False for watched")

    elif watched:
        data["watched"].append(name)
        open_write(data)
    else:
        data["pending"].append(name)
        open_write(data)

    return None
