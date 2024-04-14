def ispalindrome(n, palindrome):
    for i in range(n):
        if palindrome[i] != palindrome[n - i - 1]:
            return False
    return True


n = int(input("Enter the number of elements in the list"))

list = []

print("Enter the elements in the list")

for i in range(n):
    list.append(input())

for i in list:
    print(i, "is Palindrome", ispalindrome(len(i), i))
