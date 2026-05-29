#wap to count uppercase lowercase digits and specialchar in a string
s="PythoN 3.15!!!"
lcount=0
ucount=0
dcount=0
scount=0
for char  in s:
    if char.islower() :
        lcount+=1
    elif char.isupper():
        ucount+=1
    elif char.isdigit():
        dcount+=1
    else:
        scount+=1
print("Number of lower case",lcount)         
print("Number of upper case",ucount)    
print("Number of digit",dcount)    
print("Number of special case",scount)           
