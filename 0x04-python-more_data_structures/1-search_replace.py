#!/usr/bin/python3
def search_replace(my_list, search, replace):
    updatedList = [replace if search == newData else newData for newData in my_list]
    return updatedList
