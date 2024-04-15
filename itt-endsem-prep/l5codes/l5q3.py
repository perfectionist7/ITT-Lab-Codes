print("Enter the matrix 1:")

arr = []

for i in range(3):
    transaction = []
    for j in range(3):
        transaction.append(int(input()))
    arr.append(transaction)

arr2 = []

print("Enter the second matrix")

for i in range(3):
    transaction = []
    for j in range(3):
        transaction.append(int(input()))
    arr2.append(transaction)

print("The multiplication of the 2 matricies is: ")

result = []

for i in range(3):
    transaction = []
    for j in range(3):
        transaction.append(0)
    result.append(transaction)

for i in range(len(arr)):
    for j in range(len(arr2[0])):
        for k in range(len(arr2)):
            result[i][j] += arr[i][k] * arr2[k][j]

print(result)
