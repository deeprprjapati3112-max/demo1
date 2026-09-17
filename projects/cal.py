# simple cal.

number1 = int (input("enter the number n1:"))

number2 = int (input("enter the number n2:"))


print("choose  operator :")
print("  1 , addtion (+) ")
print("  2 ,subtraction (-) ")
print("  3 , moduler (%) ")
print("  4 , multiplication (*) ")
print("  5 , division (/) ")

choice = input("enter the choose (1/2/3/4/5): ")



if(1):
   print("addtion",number1 + number2)
   
elif(2):  
   print("subtraction ",number1 - number2) 
   
elif(3):
   print("moduler",number1 % number2)    

elif(4):
   print("multiplication",number1 * number2)
   
elif(5):
   print("division",number1 / number2)
     
else:
   print("none choosen option ")   
