def isPalindrome(k, n):
    for i in range(0, k):
        if n[i] != n[k - i - 1]:
            return False
    return True


n = input("Enter the string: ")

k = len(n)

print(n, "is Palindrome? ", isPalindrome(k, n))
