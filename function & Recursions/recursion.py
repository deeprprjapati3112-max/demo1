''' 
factorial (1) = 1
factorial (0) = 1
factorial (2) = 1*2
factorial (3) = 6
factorial (n) = n*( n-1 )*......*3*2*1

#this all the recursiion formula 
'''
# factorial (n) = n * factorial ( n-1 )

def factorial (n): 
    if ( n==1 or n==0 ):
     return 1
    return n * factorial(n-1)

n = int ( input("enter the number :"))
print(f"the factorial of this number is : { factorial (n)}")
