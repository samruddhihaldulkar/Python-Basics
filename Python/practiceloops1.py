''''Print all even numbers from 1 to 50 using while.
Print all odd numbers from 1 to 50.
Find the sum of first n natural numbers using while.
Find the factorial of a number using while.
Reverse a number using Python while.
Count digits in a number using while.
Check if a number is palindrome using while.
'''
'''i=1
while i<=50:
    if i%2==0:
        print(i)
    i+=1

i=1
while i<=50:
    if i%2 !=0:
        print(i)
    i+=1
n=int(input("enter a number:"))
i=1
sum=0
while i<=n:
    sum+=i
    i+=1
print("sum of first",n,"natural numbers is",sum)

i=1
fact=1
n=int(input("enter a number:"))
while i<=n:
    fact*=i
    i+=1        
print("factorial of",n,"is",fact)

#descending order
n=int(input("Enter a number:"))
i = n
while i >= 1:
    print(i)
    i -= 1
#Reverse a number using Python while.
n=int(input("Enter a number:"))
i=0
while n>0:
    j= n%10
    i=i*10+j
    n=n//10
print("Reversed num= ",i)

#Count digits in a number using while.

n=int(input("Enter a number:"))
count=0
while n>0:
    n=n//10
    count+=1
print("Number of digits= ",count)

#Check if a number is palindrome using while.
n=int(input("Enter a number:"))
reverse=0
original=n
while n>0:
    digit=n%10
    reverse=reverse*10+digit
    n=n//10
if reverse==original:
    print("The number is a palindrome.")
else:
    print("The number is not a palindrome.")'''

#pattern 
i=1
while i<=5:
    j=1
    while j<=i:
        print(j,end="")
        j+=1
    print()
    i+=1
