#generate a simple calculator that takes input from a user and generates output accordingly.

x=int(input("Enter a number:"))
y=int(input("Enter a number:"))
z=x+y,x*y,x/y,x-y,x%y,x//y
print("Answer is :",z)
print("Add is : ",x+y)
print("Sub is : ",x-y)
print("Mul is : ",x*y)
print("Div is : ",x/y)
print("Rem is : ",x%y)
print("INT DIV is : ",x//y)
#input function prevents the rpogram from terminating instantly and waits for user confirmation
input("The operation completes here ,press enter to terminate the program")