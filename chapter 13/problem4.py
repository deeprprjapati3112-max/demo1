
def divisiable5(n):
    if (n%5 ==0):
        return True
    return False

a = [ 1251,54,45,45,75,55]

f = list(filter(divisiable5,a))
print(f)