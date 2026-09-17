age = 20

if age >= 18:    # if else
    print("Adult")
elif age == 17:
    print("Almost Adult")
else:
    print("Minor")

print(age >= 18 and age < 60)
print(age < 18 or age > 60)
print(not(age < 18))