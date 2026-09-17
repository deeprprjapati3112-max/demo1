num = int(input("Enter a number: "))

reverse = 0

while 0 < num :
    digit = num % 10  # take the last digit
    
    reverse = reverse * 10 + digit       # reverse number
    
    num = num // 10    # remove the last digit 

print("Reverse =", reverse)