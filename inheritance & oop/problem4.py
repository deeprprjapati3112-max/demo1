# class employee:
#     salary = 20000
#     increment = 25
 
#     @property
#     def salaryAfterIncreament(self): 
#       return self.salary + self.salary *(self.increment /100)

# e = employee()
# print(e.salaryAfterIncrement)

class employee:
    salary = 20000
    increment = 20

    @property
    
    def salaryAfterIncrement(self): # new salary
        return self.salary + self.salary * (self.increment / 100)
    
    @salaryAfterIncrement.setter
    
    def salaryAfterIncrement(self,salary): # old salary
        self.increment = ((salary/self.salary ) -1 ) /100

e = employee()
print(e.salaryAfterIncrement)
e.salaryAfterIncrement  = 24000.0
print(e.increment)