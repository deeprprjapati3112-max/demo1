class calualator:
    def __init__(self,n):
        self.n = n 
    def square (self):
     print(f"the square is {self.n * self.n}")
    def cube (self):
     print(f"the cube is {self.n * self.n * self.n}")
    def root (self):
     print(f"the root is {self.n **1/2}")  
     
                     
    
a = calualator(12)
a.square() 
a.root()
a.cube()   