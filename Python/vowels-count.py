#wap to count the number of vowels and consonents in the string and print them seperately 
s = "hello World,i am python interpreter,its nice to meet you "
vcount = 0
for char in s:
    if char in "aeiou":
        vcount+=1
print("number of vowels",vcount)         
ccount=0
for char in s:
    if char not in "aeiou":
        ccount+=1
print("number of consonents",ccount)        