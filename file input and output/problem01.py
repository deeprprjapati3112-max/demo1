f = open ("poem.txt")
content =f.read()
if ("twinkle "in content):
    print("the word of the twinkle in the content")
else :
    print("in this poem not any twinkkle name later")    
f.close()