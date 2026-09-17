numbers = [12, 45, 7, 89, 34, 56]

largest = numbers[0]

for num in numbers:
    if num > largest:       # large
        largest = num

print("Largest =", largest)