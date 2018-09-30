"""
Delete a movie entry from database
"""
import json
from JSON_handler import read_JSON

def open_write(data):
    with open("A:\Coding projects\main projects folder\movie_record\JSON_handler\data.json", "w") as fileopen:
        json.dump(data, fileopen)

def delete_data(watched, name):
    data = read_JSON.get_data()

    if type(watched) != bool:
        print("Please state either True or False for watched")

    elif watched:
        # check if name is in database
        try:
            data["watched"].remove(name)
        except:
            print(f"The movie:{name} was not found in database")
            # write to database
        else:
            open_write(data)

    else:
        # check if name is in database
        try:
            data["pending"].remove(name)
        except:
            print(f"The movie:{name} was not found in database")
        # write to database
        else:
            open_write(data)
