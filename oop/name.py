class employee:
    
    lang = " python"#class attributes
    
    salary = 1200000
    
deep = employee() 
deep.name = " dipu "
print(deep.name,employee.lang,employee.salary) # this is instance attributes

janvi = employee()
janvi.name = " janu"
print(janvi.name,employee.lang,employee.salary)

# here name is a object  instance attributes and salary and lang are the class 
# attributes as they directly belong to the class 