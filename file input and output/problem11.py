with open ("file2.txt")as f:  # main old file 
    content = f.read()
 
 
with open ("file1.txt","w")as f:  # after converrt 
    
    f.write(content)   