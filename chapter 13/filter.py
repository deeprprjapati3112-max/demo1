l = [1,2,34,45,54]

def even (n):
    if n%2==0:
        return True
    else:
        return False

onlyeven = list(filter(even,l))
print(onlyeven)
