def square_matrix_simple(matrix=[]):
    newMatrix = []
    for item in matrix:
        for i in item:
            x = i ** 2 
            newMatrix.append([x])
    return newMatrix
