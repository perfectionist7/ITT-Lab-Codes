def removepunctuation(a, k):
    b = ""
    for i in k:
        if i not in a:
            b += i
    return b


a = [",", '"', ".", ":"]
k = input("Enter the string")

print("without puncuation ", removepunctuation(a, k))
