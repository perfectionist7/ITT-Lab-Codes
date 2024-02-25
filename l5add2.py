n = int(input("Enter the length of the list"))

print("Enter the elements of the list")
arr = [0] * n

for i in range(n):
    arr[i] = int(input())

for i in range(n):
    for j in range(i + 1, n):
        if arr[i] > arr[j]:
            t = arr[i]
            arr[i] = arr[j]
            arr[j] = t

print(arr)
