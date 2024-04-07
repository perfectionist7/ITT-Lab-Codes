n = int(input("Enter the number of elements in the list : "))

print("Enter the elements of the list: ")

arr = [0] * n
reverse = []
for i in range(n):
    arr[i] = int(input())

flag = 0
for i in range(n):
    if arr[i] == arr[n - i - 1]:
        continue
    else:
        flag = 1

if flag == 1:
    print("Not a Palindrome")
else:
    print("Palindrome")
