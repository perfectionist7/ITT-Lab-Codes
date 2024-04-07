n = [2, 1, 2, 3, 4, 2]

for i in range(len(n)):
    for j in range(i + 1, len(n) - 1):
        if n[i] == n[j]:
            n.pop(j)

print(n)
