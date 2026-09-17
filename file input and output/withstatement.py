f = open ("myfile.txt")
print(f.read())

f.close()

# same write a using of the with statement 
with open ("myfile.txt") as f :
    
    print(f.read())
    
    # and the auto matically close the file