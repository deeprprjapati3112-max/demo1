result = {}   # use of the dict 

subject1_name = input("enter the name of subject 1:")
result.update({subject1_name: int(input("enter the markes of subject 1:"))})

subject2_name = input("enter the name of subject 2:")
result.update({subject2_name: int(input("enter the markes of subject 2:"))})

subject3_name = input("enter the name of subject 3:")
result.update({subject3_name: int(input("enter the markes of subject 3:"))})

subject4_name = input("enter the name of subject 4:")
result.update({subject4_name: int(input("enter the markes of subject 4:"))})

subject5_name = input("enter the name of subject 5:")
result.update({subject5_name: int(input("enter the markes of subject 5:"))})




if (list(result.values())[0],list(result.values())[1],list(result.values())[2],list(result.values())[3],list(result.values())[4] )< 33:
    print("you are the fail",subject1_name,subject2_name,subject3_name,subject4_name)
    
elif (list(result.values())[0],list(result.values())[1],list(result.values())[2],list(result.values())[3],list(result.values())[4] )< 50:
    
    print("you are only pass",subject1_name,subject2_name,subject3_name,subject4_name)    
  
elif (list(result.values())[0],list(result.values())[1],list(result.values())[2],list(result.values())[3],list(result.values())[4] )< 60:
    
    print("you are pass",subject1_name,subject2_name,subject3_name,subject4_name)    
    
elif (list(result.values())[0],list(result.values())[1],list(result.values())[2],list(result.values())[3],list(result.values())[4] )< 70:
    
    print("you are  pass and nice",subject1_name,subject2_name,subject3_name,subject4_name)     
    
elif (list(result.values())[0],list(result.values())[1],list(result.values())[2],list(result.values())[3],list(result.values())[4] )< 80:
    
    print("you are  pass, good",subject1_name,subject2_name,subject3_name,subject4_name)     
    
elif (list(result.values())[0],list(result.values())[1],list(result.values())[2],list(result.values())[3],list(result.values())[4] )< 90:
    
    print("you are pass,exllant",subject1_name,subject2_name,subject3_name,subject4_name)    
    
else:
    
    print("you are top very good",subject1_name,subject2_name,subject3_name,subject4_name)  
    
print("percentage of the student ",(sum (result.values()))/500*100)  

if (any (i<33 for i in result.values())):
    print("you are the fail in the subject",subject1_name,subject2_name,subject3_name,subject4_name)      
    
else:
    print("congres you are pass in all subject ",result.keys())    