class employee:
    company = "apple"
    nmae = "deep"                       #parent 1 
    def show (self):
        print(f"The name is {self.name} and the comapany is {self.company}")
        
class coder:
    language = "python"
    def printlanguage(self):            #parent 2
         print(f"The name is and he is good : {self.language}")
   
   
class programer (employee,coder):
    company = "apple"
    name = "deep"                        #child
    def showlanguage (self):
       print(f"the name is {self.comapany} and he is good with  language :{self.language}") 
          
a = employee()
b = programer()
b.show()
b.printlanguage()
