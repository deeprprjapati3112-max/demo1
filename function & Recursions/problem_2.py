def f_to_c (f):
    c =5*(f-32)/9
    return c

f = int (input("enter the temp in f:"))    
c = f_to_c(f)
print(f"{round(c, 2)}°C")