n = int(input("enter the a number : "))

for  i in range ( 2,n ):
    if ( n%i ) == 0 :
        print (" number is the not prime ")
        break
    else : 
      print("number is the prime ") 
    #   ✅ Prime: 2, 3, 5, 7, 11, 13
    #   ❌ Not Prime: 4, 6, 8, 9, 10