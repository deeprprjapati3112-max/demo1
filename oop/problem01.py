class programer:
    company = " apple "
    def __init__(self , name , salary , work): # __Init__ use for the explain info 
     self.name = name  # explain the info about the give company employee
     self.salary= salary
     self.work = work
        
        
p = programer("deep",125000,"data science")

print(p.name,p.salary,p.work,p.company)   


class collage:
    name = "cvm"
    
    def __init__(student,name,no,betch):
      student.name = name
      student.no = no
      student.betch = betch
        
s = collage ( "deep",1224,"A")   
print(s.name,s.no,s.betch)     
        
        