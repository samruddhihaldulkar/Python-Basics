num = [1,2,3,4,5,6,7,8,9,10]
i = 0
x = 11

while i < len(num):
    if num[i] == x:
        print("found", i)
        break
    i += 1
else:
    print("not found")    
    
       