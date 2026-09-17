class employee:
    
    lang = " python"     # this are the call class attribute
    salary = 1200000
    name = "deep"
 
    
deep = employee()        # to same defind

employee.name = deep     # this is the object instance  attribute  and print this in output
print(employee.salary,employee.lang,employee.salary,employee.name) 

krupa = employee()  
                         
print(employee.salary,employee.lang)
