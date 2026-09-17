word = " janvi "

with open ("lovefile.txt",)as f:   # read first 
    content = f.read ()
    
contentnew  = content.replace ( word , "deep i love you")    # replace 
 
with open ("lovefile.txt","w")as f: # new contant write 
    f.write(contentnew)