with open ("this.txt")as f:
    content = f.read()       # for read file 
    
with open ("this_copy.txt","w")as f:     # for write file 
    f.write(content)    