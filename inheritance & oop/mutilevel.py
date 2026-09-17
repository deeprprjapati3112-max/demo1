class employee:
    a = 1
class programer(employee):
    b = 2 
class manger(programer):
    c = 3
    
o = employee()
print(o.a)
#print(o.b)has be not in a employee class so that make error

o = programer()
print(o.a,o.b)

o = manger ()
print(o.a,o.b,o.c)
        
    