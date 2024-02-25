n = input("Enter the string ")

arr = n.split(" ")
res = [0] * len(arr)
dict = {}

for i in arr:
    if i in dict:
        dict[i] += 1
    else:
        dict[i] = 1
print(len(arr))
print(dict)
