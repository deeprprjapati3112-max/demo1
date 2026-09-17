#initial in this IN USE OF   [     IN KEY WORD     ]
p1 ="make lot of money"
p2 ="buy now"
p3 ="click this"
p4 ="do now"
p5 ="open link"

massage = input ("enter the your comment:")

if ((p1 in massage ) or (p2 in massage) or (p3 in massage) or( p4 in massage) or (p5 in massage)):
   print("This comand is spam ")
   
else:
     print("This coamd is not a spam ")