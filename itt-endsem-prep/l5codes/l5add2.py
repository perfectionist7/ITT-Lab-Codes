n = int(input("Enter the number of elements in the list"))

print("Enter the elments in the list")

arr = []
for i in range(n):
    arr.append(int(input()))


for i in range(0, len(arr)):
    for j in range(0, len(arr)):
        if arr[j] > arr[i]:
            arr[i], arr[j] = arr[j], arr[i]

print(arr)
