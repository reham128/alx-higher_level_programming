#!/usr/bin/env python3
def no_c(my_string):
    strlen = len(my_string)
    count = ''
    for a in my_string:
        if (my_string != 'C' and my_string != 'c'):
            count = count + a
    return count
