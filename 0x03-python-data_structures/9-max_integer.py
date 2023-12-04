#!/usr/bin/python3
def max_integer(my_list=[]):
    length = len(my_list)
    if length < 1:
        return None
    maxV = my_list[0]
    for i in my_list[1:]:
        if i > maxV:
            maxV = i
    return maxV
