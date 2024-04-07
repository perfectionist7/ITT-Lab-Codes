print("Enter the number of numbers: ")
n = int(input())
arr = [0] * n
count = 0
print("Enter the prime numbers: ")
for i in range(n):
    arr[i] = int(input())

print("Prime numbers are: ")
for i in arr:
    flag = 0
    for j in range(2, i):
        if i % j == 0:
            flag = 1
    if flag == 0:
        print(i, end=" ")
        count += 1

print("Count is ", count)
