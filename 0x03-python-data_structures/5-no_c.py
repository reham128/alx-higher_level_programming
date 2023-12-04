#!/usr/bin/env python3
def no_c(my_string):
    count = ""
    for string  in my_string:
        if (string != 'C' and string != 'c'):
            count = count + string
        return count
