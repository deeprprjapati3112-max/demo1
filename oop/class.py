class employee:
    
    name = " deep "
    lang = " python"     # this are call class attribute
    salary = 1200000
    
deep = employee() 
# employee.name = deep       # this are call object attribute
print(employee.name,employee.lang)   


class company:
    
    name = " google "
    salary = 4000000
    
google = company()

print(company.name ,company.salary)    

class love:
    man = "deep"
    woman = "none"
    
deep = love()
none = love()
print(love.man,love.woman)    
        
        
    