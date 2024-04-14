list = [2, 3, 1, 2, 3]

arr = [0] * len(list)

k = len(list) - 1
for i in range(len(list)):
    arr[k - i] = list[i]

print(arr)
