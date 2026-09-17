    
n = int(input("Enter a number: "))

fact = 1

for i in range(1, n + 1): # find the no fact
    fact *= i

print("Factorial =", fact)