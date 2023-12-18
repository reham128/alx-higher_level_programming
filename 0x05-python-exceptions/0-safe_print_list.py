#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    counter = 0
    for a in my_list:
            if counter < x:
                try:
                    print(a, end='')
                    counter = counter + 1
                except IndexError:
                    break
    print()
    return counter
