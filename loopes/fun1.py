# for i in range(0,20):
#     print(i)           # print the 1 to 20 
    
# for i in range (0,51):
#     if (i%2==0):         # even number 
#         print(i)
#     else :
#         print("old number")
        
# for i in range (0,101):
#     if (i%3==0 and i%5==0):
#         print(i)

n = int (input("enter the number:"))

for i in range (1,n+1):
    if(i==1 or i==n):
        print("*"*n ,end = "")
    else:
        print("*",end = "")
        print(" "*(n-2),end = "")
        print("*",end = "")
    print("")
            