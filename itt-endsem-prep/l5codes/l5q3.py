mat1 = [[1, 3, 4], [2, 3, 5], [3, 2, 7]]
mat2 = [[6, 5, 2], [3, 3, 4], [3, 2, 3]]
result = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]


for i in range(len(mat1)):
    for j in range(len(mat1[0])):
        for k in range(len(mat1)):
            result[i][j] += mat1[i][k] * mat2[k][j]


print(result)
