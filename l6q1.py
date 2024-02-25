str1 = input("Enter the string")

newstr = ""
for i in str1[::-1]:
    newstr += i


if newstr == str1:
    print("Palindrome")
else:
    print("Not a Palindrome")
s
