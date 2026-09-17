from functools import reduce

l = [ 1251,54,45,45,75,55,5454,431]

def greter(a,b):
    if (a>b):
        return a
    return b

print(reduce(greter,l))

