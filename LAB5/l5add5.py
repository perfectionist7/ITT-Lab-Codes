arr = [1, 2, 4, 2, 3]
n = len(arr)
newarr = [0] * n
k = 0
for i in arr[::-1]:
    newarr[k] = i
    k += 1


print(newarr)
