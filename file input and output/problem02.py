import random

def game (): 
    print ("you are the playing the game.. ") # i am import the random number 
    score = random.randint(1,62)
    
    with open ("hiscore.txt") as f:
       hiscore= f.read ()      # declare the hiscore file 
       if (hiscore!=""):
         hiscore= int(hiscore) 
       else :
         hiscore = 0 
         
    print(f"your score : {score}")
    if ( score > hiscore):
                                             # print the guess number 
     with open ("hiscore.txt","w") as f :
        f.write(str(score))
        
    return score
game()  
                 