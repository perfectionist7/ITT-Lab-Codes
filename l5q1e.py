def natural(n):
    if n == 0:
        return 0
    return n + natural(n - 1)


n = int(input("Enter the number: "))
print(natural(n))
