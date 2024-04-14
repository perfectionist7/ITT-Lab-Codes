def sumlist(arr, n):
    if n == -1:
        return 0
    return arr[n] + sumlist(arr, n - 1)


n = int(input("Enter the length of the list"))

print("Enter the elements in the list")
arr = []
for i in range(n):
    arr.append(int(input()))

print(sumlist(arr, n - 1))
