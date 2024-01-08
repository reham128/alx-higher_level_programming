#!/usr/bin/python3
'''mylist class that inherits from list'''


class MyList(list):
    '''subclass start'''
    def print_sorted(self):
        '''to print the list after sorted'''
        print(sorted(self))
