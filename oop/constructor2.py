class employee:
    language = "python"
    salary = 120000         
    
    def __init__(self,name ,salary,language): # this are the constructor to use in the 
        # is dunder method it is call as automatically
        
        self.name = name
        self.salary = salary
        self.language = language
        print("i love you too janvi")
    
    
    def getinfo(self):
        
            
        print(f"the language is { self.language } the salary is { self.salary}")
    
    def greet(self):
        print("good night i love you janvi")    
        
deep = employee("deep",123244,"java")
employee.name = " deep "
print(employee.name)     

employee.getinfo (deep)
employee.greet(deep)

#def __init__(self,name ,salary,language): # this are the constructor to use in the 
        # is dunder method it is call as automatically
        
       #  self.name = name
        # self.salary = salary
        # self.language = language

#deep.getinfo()