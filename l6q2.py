arr = ",:."

n = input("Enter the string: ")

newstr = ""

k = 0

for i in n:
    if arr.count(i) > 0:
        n = n.replace(i, "")

print(n)
