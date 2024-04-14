arr = []
for i in range(3):
    transcations = []
    for j in range(3):
        transcations.append(int(input()))
    arr.append(transcations)

print("Matrix: \n")
print(arr)

newarr = []
for i in range(3):
    transcationsn = []
    for j in range(3):
        transcationsn.append(0)
    newarr.append(transcationsn)

for i in range(3):
    for j in range(3):
        newarr[i][j] = arr[j][i]

print("Transpose")
print(newarr)
