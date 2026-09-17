def genratetable(n):
    table= ""
    for i in range (1,11):
        table += f"{n}*{i} = {n*i}\n"
        
        
    with open (f"table.txt/table_{n}","w")as f:
        f.write(table)
        
for i  in range ( 2,21):
    genratetable(i)
            
        