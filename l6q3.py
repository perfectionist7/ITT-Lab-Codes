strlist = input("Enter the string")

str1 = list(strlist)
for i in range(len(str1)):
    for j in range(i + 1, len(str1)):
        if ord(str1[j]) < ord(str1[i]):
            str1[i], str1[j] = str1[j], str1[i]

finalstr = ""
for i in str1:
    finalstr += i

print(finalstr)
