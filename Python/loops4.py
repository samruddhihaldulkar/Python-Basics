n=int(input("Enter the number n: "))
a=0
b=1
for i in range(n):
    print(" ",a," ")
    temp=a
    a=a+b
    b=temp
    