#!/usr/bin/python3
"""Import JSON and save_to_join_file & load_from_json_file function"""


import json
save_to_json_file = __import__("5-save_to_json_file").save_to_json_file
load_from_json_file = __import__("6-load_from_json_file").load_from_json_file
from sys import argv


filename = "add_item.json"

try:
    json_list = load_from_json_file(filename)
except:
    json_list = []
for arg in argv[1:]:
    json_list.append(arg)
save_to_json_file(json_list, filename)
