n = input("Enter the string")

n1 = list(n)
f = input("Enter the character to find")
g = input("Enter the chracter to replace it with")

for i in range(len(n1)):
    if f == n1[i]:
        n1[i] = g


finalstr = "".join(n1)

print(finalstr)
