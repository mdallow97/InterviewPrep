# search_matrix.py

def searchMatrix(matrix, target):
    for line in matrix:
        if target in line:
            return True

    else:
        return False

def searchMatrix2(matrix, target):
    '''
    [
      [1,   4,  7, 11, 15],
      [2,   5,  8, 12, 19],
      [3,   6,  9, 16, 22],
      [10, 13, 14, 17, 24],
      [18, 21, 23, 26, 30]
    ]
    '''
    # start top right
    i = 0
    j = len(matrix[0])-1

    for line in matrix:
        print(line)

    while i <= len(matrix)-1 and j >= 0:
        if matrix[i][j] == target:
            return True

        if matrix[i][j] < target:
            i += 1
        else:
            j -= 1

    return False


matrix = [[1,4,7,11,15], [2,5,8,12,19], [3,6,9,16,22], [10,13,14,17,24], [18,21,23,26,30]]

print(searchMatrix2(matrix, 1))
