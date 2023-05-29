#Write an algorithm such that if an elerment in an MxM matrix is 0, its entire row and column are set to 0
import copy
def ZeroMatrix(matrix):
    matrixOut = copy.deepcopy(matrix)

    countRows = 0
    while countRows < len(matrix):
        countColumn = 0
        while countColumn < len(matrix[0]):
            if matrix[countRows][countColumn] == 0:  
                rowAssign = 0
                while rowAssign < len(matrix):
                    matrixOut[rowAssign][countColumn] = 0
                    rowAssign += 1
                colAssign = 0
                while colAssign < len(matrix[0]):
                    matrixOut[countRows][colAssign] = 0
                    colAssign += 1

            countColumn += 1
        countRows += 1
    return matrixOut

sampleMatrix1 = [[0, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]]
print(ZeroMatrix(sampleMatrix1))