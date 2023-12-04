#!/usr/bin/env python3
def no_c(my_string):
    strlen = len(my_string)
    count = ''
    for a in range(strlen):
        if (my_string[a] != 'C' and my_string[a] != 'c'):
            count = count + my_string[a]
    return count
