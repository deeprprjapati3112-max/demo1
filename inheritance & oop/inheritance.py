class employee:
    company = "apple"
                                          #parent 1
    def show (self):
        
        print(f"The name is {self.name} and the salary is {self.name}")
           
class programer (employee):
    company = "apple" 
    name = "Deep"
    language = "python"
    def show (self):              # child 1
        
       print(f"the name is {self.name} and he is good with {self.language}language") 
          
a = employee()
b = programer()

print(a.company,b.company,b.name) 
b.show()

             