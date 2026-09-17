a = ( int( input ("enter the number :")))
b = ( int( input ("enter the number :")))
c = ( int(input("enter the number :")))


def larger(a,b,c):
    if a>b and a>c:
        return a
    elif b>a and b>c:
        return b 
    else :
        return c
ans = larger(a,b,c)
print("lager number ",ans)

