'''
write a python program to input age of two users and print who is older and who is younger.
'''
age1=int(input("Enter age of first user: "))
age2=int(input("Enter age of second user: "))
if age1>age2:
    print("First user is older than second user.")
elif age2>age1:
    print("Second user is older than first user.")
else:
    print("Both users are of the same age.")