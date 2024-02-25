str1 = "Mississippi Alabama Texas Massachusetts Kansas"

statesList = [0] * 5
newlist = str1.split(" ")
flag = 0

for i in newlist:
    n = len(i)
    k = i[n - 3 : n]
    if k == "xas":
        statesList[0] = i
    if i[0].lower() == "k":
        statesList[1] = i

    if i[0] == "M" and i[-1] == "s":
        statesList[2] = i
    if i[-1] == "a":
        statesList[3] = i
    if flag == 0 and i[0] == "M":
        statesList[4] = i
        flag = 1
print(statesList)
