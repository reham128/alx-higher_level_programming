#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if matrix:
        for e in matrix:
            mLen = len(e)
            if mLen == 0:
                print()
            for a in range(mLen):
                print('{:d}'.format(e[a]), end='\n' if a is mLen - 1 else ' ')
    else:
        return None
