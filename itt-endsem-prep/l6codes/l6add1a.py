s = "Mississippi Alabama Texas Massachusetts Kansas"
statesList = [0] * 5

k = s.split(" ")
flag = 0
for i in k:
    n = len(i)

    b = i[n - 3 : n]
    if i[0] == "M" and flag == 0:
        statesList[4] = i
        flag = 1
    if b == "xas":
        statesList[0] = i
    if i[0] == "K" and i[len(i) - 1] == "s":
        statesList[1] = i
    if i[0] == "M" and i[len(i) - 1] == "s":
        statesList[2] = i
    if i[len(i) - 1] == "a":
        statesList[3] = i


print(statesList)
