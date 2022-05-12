def diagonalDifference(arr):
    d1 = []
    d2 = []
    reverse = -1
    for i in range(len(arr)):
        d1.append(arr[i][i])
        d2.append(arr[i][reverse])
        reverse -= 1


    return abs(sum(d1) - sum(d2))




matrix = [[11, 2, 4], [4, 5, 6], [10, 8, -12]]
print(diagonalDifference(matrix))