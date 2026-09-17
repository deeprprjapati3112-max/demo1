for num in range(2, 101):
    is_prime = True

    for i in range(2, num):
        if num % i == 0:
            is_prime = False   # odd even number 
            break

    if is_prime:
        print(num)