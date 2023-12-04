#!/usr/bin/env python3
def no_c(my_string):
    strlen = len(my_string)
    count = ''
    for a in my_string:
        if (a != 'C' and a != 'c'):
            count = count + a
    return count
