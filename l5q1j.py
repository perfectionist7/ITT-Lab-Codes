str = input("Enter the string: ")

arr = str.split(" ")

for i in arr:
    for j in i:
        k = ord(j) + 3
        if k > 90:
            k = k - 26
        print(chr(k), end="")

    print(" ")
