def naturalnum(n):
    if n == 0:
        return 0
    return n + naturalnum(n - 1)


print(naturalnum(5))
