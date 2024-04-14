def fibonacci(n):
    arr = []
    a = 0
    b = 1
    if n == 0:
        return a
    if n == 1:
        return a, b
    else:
        arr.append(a)
        arr.append(b)
        for i in range(2, n):
            c = a + b
            arr.append(c)
            a = b
            b = c
        return arr


def fiboatplace(n):
    a = 0
    b = 1
    fibosum = 1
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        for i in range(2, n):
            c = a + b
            fibosum += c
            a = b
            b = c
        return fibosum


def fibo(n):
    if n <= 1:
        return n
    return fibo(n - 1) + fibo(n - 2)


print(fibonacci(5))
print(fiboatplace(5))
print(fibo(6))
