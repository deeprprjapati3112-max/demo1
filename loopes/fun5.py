n = int(input("enter the number :"))

odd = 0 
even= 0 

for i in range( 1 , n +1 ):
    if(i%2==0):
        even +=1          # number odd or even 
        
    
    else:
        odd += 1

print("Even =", even)  # in this code to divide the no odd and even 
print("Odd =", odd)