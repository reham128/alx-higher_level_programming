#!/usr/bin/python3
'''function to divid all elements of a matrix'''


def matrix_divided(matrix, div):
    '''to divide by value of div to return a new matrix
    list f list'''
    if not isinstance(matrix, list) or len(matrix) == 0 or not matrix[0]:
        raise TypeError('matrix must be a matrix (list of lists)' +
                ' of integers/floats')
    if not isinstance(div, (int, float)):
        raise TypeError('div must be a number')

    for raw in matrix:
        if not isinstance(raw, list) or len(raw) == 0:
            raise TypeError('matrix must be a matrix (list of lists)' +
                    ' of integers/floats')
        for colum in raw:
            if not isinstance(colum, (int, float)):
                raise TypeError('matrix must be a matrix (list of lists)' +
                        ' of integers/floats')

        if len(raw) != len(matrix[0]):
            raise TypeError('Each row of the matrix must have the same size')

    return [[round(colum / div, 2) for colum in raw] for raw in matrix]

if __name__ == '__main__':
    import doctest
    doctest.testfile('tests/2-matrix_divided.txt')
