#!/usr/bin/python3
"""Finde a peak in unsorted int list"""


def find_peak(list_of_integers):
    """to find a peak in unsorted int list"""
    if len(list_of_integers) == 0:
        return (None)
    if len(list_of_integers) == 1:
        return (list_of_integers[0])
    if len(list_of_integers) == 2:
        return (max(list_of_integers))
    low = 0
    high = len(list_of_integers) - 1

    while low < high:
        mid = (low + high) // 2

        if (list_of_integers[mid]) < (list_of_integers[mid + 1]):
            low = mid + 1
        else:
            high = mid

    return (list_of_integers[low])
