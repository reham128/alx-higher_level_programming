#!/usr/bin/python3
'''function to return lis of lists of integers in form of
Pascal’s triangle of n'''


def pascal_triangle(n):
    '''n is size of the output triangle'''
    if n <= 0:
        return []

    output = [[1]]
    out_len = len(output)
    while out_len != n:
        a = output[-1]
        last = [1]
        a_len = len(a)
        for i in range(a_len - 1):
            last.append(a[i] + a[i + 1])
        last.append(1)
        output.append(last)
    return (output)
