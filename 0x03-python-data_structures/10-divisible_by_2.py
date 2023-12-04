#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    if not my_list:
        return None
    else:
        output = []
        for element in my_list:
            if element % 2 == 0:
                output.append(True)
            else:
                output.append(False)
        return output
