arr = [2, 3, 4, 1, 2, 1]

uniq = {}
for i in arr:
    if i not in uniq:
        uniq[i] = 1
    else:
        uniq[i] += 1

for value, count in uniq.items():
    print(value)
