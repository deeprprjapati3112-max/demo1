try:
    a = int(input("hi i am deep and what is your age :"))
    print(a)
    
except ValueError as v :
    print("error")
    print(v) 
    

except Exception as e :    
    print(e)
    
    print( "!!! thank you try one more time")