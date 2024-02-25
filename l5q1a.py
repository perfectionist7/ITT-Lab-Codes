while 1:
    a = int(input("Enter the first number"))
    b = int(input("Enter the second number"))
    c = input("Enter the operation to be performed (*,/,+,-)")

    if c == "*":
        print("The answer is ", a * b)
    elif c == "-":
        print("The answer is ", a - b)
    elif c == "+":
        print("The answer is ", a + b)
    elif c == "/":
        print("The answer is ", a / b)
    else:
        print("Please enter only from the options")
    d = int(input("Enter -1 to exit and any other key to continue"))
    if d == -1:
        break
    else:
        continue
