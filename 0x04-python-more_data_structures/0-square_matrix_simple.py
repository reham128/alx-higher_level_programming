def square_matrix_simple(matrix=[]):
    newMatrix = []
    for item in matrix:
        newMatrix.append([i ** 2 for i in item])
    return newMatrix
