# Function
def add(a, b):
    return a + b

print(add(10, 20))

# Default Argument
def greet(name="Deep"):
    print("Hello", name)

greet()
greet("Rahul")

# Recursion
def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n - 1)

print(factorial(5))