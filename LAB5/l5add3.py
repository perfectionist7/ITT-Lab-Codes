def sum(n, size):
    if size == 0:
        return 0

    return n[size - 1] + sum(n, size - 1)


a = [2, 3, 1, 2, 3]
print(sum(a, len(a)))
