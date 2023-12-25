#!/usr/bin/python3
def print_last_digit(number):
    number = abs(number)
    lastDig = number % 10
    print("{}".format(lastDig), end='')
    return (lastDig)
