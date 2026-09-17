class employee:
    a = 1
    def __init__(self):
        print("constructor of the employee")
class programer(employee):
    
    def __init__(self):
        print("constructor of the programer")
    b = 2 
class manger(programer):
    def __init__(self):
        super(). __init__()#this is super class syntax to saw
        print("constructor of the manger")
    c = 3
    
o = employee()
print(o.a)
#print(o.b)has be not in a employee class so that make error

o = programer()
print(o.a,o.b)

o = manger ()
print(o.a,o.b,o.c)