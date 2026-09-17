def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b

n1 = int(input("Enter first number: "))
n2 = int(input("Enter second number: "))

choice = input("Choose (+, -, *, /): ")

if choice == "+":
    print("Answer =", add(n1, n2))
elif choice == "-":
    print("Answer =", subtract(n1, n2))
elif choice == "*":
    print("Answer =", multiply(n1, n2))
elif choice == "/":
    print("Answer =", divide(n1, n2))
else:
    print("Invalid choice")