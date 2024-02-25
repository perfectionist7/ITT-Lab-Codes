a = int(input("Enter the first number"))
b = int(input("Enter the second number"))


for i in range(a, b):
    flag = 0
    for j in range(2, i):
        if i % j == 0:
            flag = 1
    if flag == 0:
        print(i)
