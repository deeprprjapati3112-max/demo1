n = int(input("enter the number :"))
i = 1
 
for i in range(1,11):   
    # table 
    print(f"{n}*{i} = { n*i}")
    
    
    
# ✅ for loop → Don't use i += 1 (Python does it automatically.)

# ✅ while loop → You usually need i += 1, 

# otherwise the loop may never end. 