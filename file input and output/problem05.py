word = (" janvi" , "deep" , "dipali ")

with open ("file.txt","r")as f:
    content = f.read ()
for word in word:   
 content = content.replace ( word , " love " * len(word ))  

with open ("file.txt","w")as f:
    f.write(content)