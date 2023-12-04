#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    if idx >= len(my_list) or idx < 0:
        return my_list.copy()
    else:
        return my_list[0:idx] + [element] + my_list[idx + 1:]
