from random import randint

class train:
    
    def __init__(self,trainno, fro , to):
        self.trainno = trainno
        self.fro = fro
        self.to = to
        
    def book(self): #explain  
        print(f"train ticket are the booking : {self.trainno} from {self.fro} to {self. to } ")
        
    def getstatus(self ,trainno): # 
        print(f"train : {trainno} running success fully ")
        
    def getfare(self ,trainno ,fro,to):
        print (f"ticket fare in train no : { trainno } from {fro} to {to} is { randint (200,1000)}")   
       
t = train ()
t.book("guj ","mahi") 
t.getstatus()  
t.getfare("guj","mahi")   