n = int(input("Enter the order of the matrix"))

matrix1 = []
matrix2 = []
for i in range(n):
    arr = []
    for j in range(n):
        arr.append(int(input()))
    matrix1.append(arr)

for i in range(n):
    arr = []
    for j in range(n):
        arr.append(int(input()))
    matrix2.append(arr)

print("multiplicated matrix: \n")

matrix3 = [[0 for _ in range(n)] for _ in range(n)]
sum1 = 0
for i in range(n):
    for j in range(n):
        for k in range(n):
            matrix3[i][j] += matrix1[i][k] * matrix2[k][j]

for r in matrix3:
    print(r)
# 1 2 3   3 6 7     arr[i][j] * arr[j][i]
# 3 4 5   8 9 2
# 3 4 1   1 2 1

# 22
