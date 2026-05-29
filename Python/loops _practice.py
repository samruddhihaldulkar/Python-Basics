n=5
for i in range(1,n+1):
    for j in range(i):
        print(i,end="")
    print()    
for i in range(n,0,-1):
    for j in range(i):
        print(i,end="")
    print()
n=4
num=1
for i in range(1,n+1):
    for j in range(i):
        print(num,end=" ")
        num+=1
    print()