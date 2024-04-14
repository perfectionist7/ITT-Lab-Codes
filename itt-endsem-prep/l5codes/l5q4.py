mat1 = [[3, 4, 7], [5, 1, 2], [6, 3, 4]]
mat2 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

for i in range(len(mat1)):
    for j in range(len(mat1[0])):
        mat1[i][j] += mat2[i][j]


print(mat1)
