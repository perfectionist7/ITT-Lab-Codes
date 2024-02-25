n = int(input("Enter the order of the matricies"))

matrix1 = []
matrix2 = []

for i in range(n):
    arr = []
    for j in range(n):
        arr.append(int(input()))
    matrix1.append(arr)

for i in range(n):
    arr1 = []
    for j in range(n):
        arr1.append(int(input()))
    matrix2.append(arr1)

for i in range(n):
    for j in range(n):
        matrix1[i][j] += matrix2[i][j]
        print(matrix1[i][j], end=" ")
    print("\n")
