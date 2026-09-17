def prime(n):
    if n > 1:
        for i in range(2, n):
            if n % i == 0:
                return False   
        return True
    return False

n = int(input("Enter the number: "))
print(prime(n))