#!/usr/bin/python3
'''task 7 which using the 2 previous tasks'''


import sys

save_to_json_file = __import__("5-save_to_json_file").save_to_json_file
load_from_json_file = __import__("6-load_from_json_file").load_from_json_file

list_o = list(sys.argv[1:])
try:
    data = load_from_json_file("add_item.json")
except FileNotFoundError:
    data = []
data.extend(list_o)
save_to_json_file(data, "add_item.json")
