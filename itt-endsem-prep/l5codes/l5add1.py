def isprime(n):
    for i in range(2, n // 2):
        if n % i == 0:
            return False
    return True


m = int(input("Enter the value of m"))
n = int(input("Enter the value of n"))

for i in range(m, n):
    print(i, "is Prime", isprime(i))
