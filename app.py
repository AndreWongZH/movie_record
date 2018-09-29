"""
Format of JSON data:
dict = {
            watched : [List of movies],
            pending : [List of movies]
        }
"""
import os
import re
import json


pathname = input("please give pathname to your movies\n")

data = {
    "watched": [],
    "pending": []
}
for file in os.listdir(pathname):
    new_name = ""
    for i in range(4):
        pattern = "[\[(] ?[A-z0-9.]* ?[\])]"
        new_name = re.sub(pattern, "", file)
    data["watched"].append(new_name.strip())

with open('data.json', 'w') as outfile:
    json.dump(data, outfile)

