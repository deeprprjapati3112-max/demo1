
enter = (" your subject name")

markes  = int(input("enter the 1 subject markes  :: "))
markes= int(input("enter the 2 subject markes  :: ")) 
markes= int(input("enter the 3 subject markes  :: "))
markes = int(input("enter the 4 subject markes  :: "))
markes= int(input("enter the 5 subject markes  :: "))   


total_markes = (markes + markes + markes + markes + markes/5)
print("total_markes")

 
                             

if(markes<=100 and markes>=90):
   print("grade is ex // very good exllent ")
  
elif(markes<=90 and markes >=80):
    print("grade is a+ //very good")   
    
elif(markes<=80 and markes >=70):
    print("grade is a // good")  
    
elif(markes<=70 and markes>=60):
    print("grade is b // ok nice")   
   
elif(markes<=60 and markes >=40):
    print("grade is c // ok but bad ") 
        
elif(markes<=40 and markes >=33):
    print("grade is d  // very bad  ") 
    
else:

    print("you are failed") 
    
    
