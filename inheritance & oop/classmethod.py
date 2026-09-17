class employee:
    a = 1
           # this is class opeartion 
    
    @classmethod
    def show (cls):  # know as the class   but insention opeartion 
        print(f"the class attribute is :{cls.a}")
        
   
e = employee() 
e.a = 45 
e.show()       # print  the  1 not 45 for use of the @classmethod  
      

