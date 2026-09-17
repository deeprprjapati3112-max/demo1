class employee:
    language = "python"
    salary = 120000 
    
    def __init__(self): # this are the constructor to use in the 
        # is dunder method it is call as automatically
        print("i love you too janvi")
    
    
    def getinfo(self):
        print(f"the language is { self.language } the salary is { self.salary}")
    
    def greet(self):               
        print("good night i love you janvi")    
        
deep = employee()
employee.name = " deep "
print(employee.name)     

employee.getinfo (deep) # this is fore declare the object 
employee.greet(deep)