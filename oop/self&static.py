
class employee:
    language = "python"
    salary = 120000 
    
    def getinfo(self):
        print(f"the language is { self.language } the salary is { self.salary}")
        
        
   
    @staticmethod  
    # this are the method to use the delete the ...
    def greet(self):
        print("good night i love you janvi")    
        
deep = employee()
employee.language = " java "
print(employee.language)     

employee.getinfo (deep)
# deep.greet()
#deep.getinfo()