a = int(input("Enter the first number"))
b = int(input("Enter the second number"))
op = input("Enter the operator ('*'/'/'/'-'/'+')")

if op == "*":
    print(a * b)
elif op == "/":
    print(a // b)
elif op == "+":
    print(a + b)
elif op == "-":
    print(a - b)
else:
    print("Incorrect operator")



