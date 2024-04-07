order = int(input("Enter the order of the matrix"))
matrix = []
for i in range(order):
    arr = []
    for j in range(order):
        arr.append(int(input()))
    matrix.append(arr)

for i in range(order):
    for j in range(i):
        t = matrix[i][j]
        matrix[i][j] = matrix[j][i]
        matrix[j][i] = t

for i in range(order):
    for j in range(order):
        print(matrix[i][j], end=" ")
    print("\n")


# 1 4 7
# 3 4 1
# 2 3 1

# 1 3 2
# 4 4 3
# 7 1 1
