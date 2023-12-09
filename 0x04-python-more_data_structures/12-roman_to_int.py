#!/usr/bin/python3
def roman_to_int(roman_string):
    if not isinstance(roman_string, str):
        return 0
    digit_data = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    all_d = 0
    i = 0
    for r in reversed(roman_string):
        i = digit_data[r]
        all_d = all_d + i if all_d < i else -i
    return all_d
