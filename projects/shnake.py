''' 
    1 for snake 
    -1 for water
    0 for gun 
    
'''

import random

computer = random.choice([1,0,-1])

print("random_number")

youstr = input ("enter the you choice (s,w,g): ")

youdict =   {"s" : 1 , "w":-1 , "g":0 }

reversedict = { 1 :" snake " , -1 :"water" , 0 :"gun"}

you = youdict[youstr] 

print(f"you chose { reversedict [you]}\n computer chose {reversedict[computer]}")

if ( computer == you ):
    print("its a draw ")
    
else:
        
    if ( computer == -1 and you == 1 ): 
      print("you are the winner ")
    
    elif ( computer == -1 and you == 0):
     print(" you are the loose ") 
       
    elif ( computer  == 1 and you == -1):
       print("you are the loose")       
 
    elif (computer == 1  and you == 0 ):
        print("you are the win")
    
    elif(computer == 0 and you == -1):
        print("you are the win")
    
    elif( computer ==0 and you == 1):
        print("you are the loose")    
    
    else:
        print("something are the wrong !! ")         