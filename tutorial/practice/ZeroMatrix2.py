def ZeroMatrix(matrix):
    rowAssign = []
    colAssign = []
    countRows = 0
    while countRows < len(matrix):
        countColumn = 0
        while countColumn < len(matrix[0]):
            if matrix[countRows][countColumn] == 0:
                rowAssign.append(countRows)
                colAssign.append(countColumn)
            countColumn += 1
        countRows += 1

    for num in colAssign:
        count = 0
        while count < len(matrix[0]):
            matrix[count][num] = 0
            count += 1


    for num in rowAssign:
        count = 0
        while count < len(matrix):
            matrix[num][count] = 0
            count += 1
    
    return matrix

sampleMatrix1 = [[0, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]]
print(ZeroMatrix(sampleMatrix1))