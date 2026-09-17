import random
n = random.randint(1,100)
a = -1
guesses = 0
while ( a!=n ):
    guesses+= 1
    a = int ( input ("guess the number  :"))
    if(a>n):
        print("lower number plz")
    else:
        print("higher number plz")

print(f"you have to guess the number in {guesses}")            