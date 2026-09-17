class complex:
    def __init__(self,r,i):
        self.r = r
        self.i = i
        
    def __add__ (self,c2 ):
        return complex(self.r + c2.r ,self.i + c2.i)  
      
    def __mul__ (self,c2):
        real_part = self.r  * c2.r - self.i * c2.i
        imag_part = self.r  * c2.r + self.i * c2.i
        return complex (real_part , imag_part)
    
    def __str__ (self):
        return f"{self.r} + { self.i }"
    
    c1 = complex (1,2)
    c2 = complex (3,4)
    print(c1 + c2)
    print(c1*c2)
