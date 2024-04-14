a = input("Enter the string to encode")
c = ""
for i in a:
    b = ord(i)
    b += 3
    if b > 122:
        b = b - 26
    c += chr(b)

print("encoded: ", c)
