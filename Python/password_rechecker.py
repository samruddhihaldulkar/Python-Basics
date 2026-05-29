correct_password = "Samruddhi@12"
atemt = 5
while atemt>0:
    new_password=input("Enter password : ")
    if new_password==correct_password:
        print("Access Granted✅")
        break
    else:
        #print("Access Denied❌")
        atemt-=1    
        print("wrong password❌")
        print("attempts left",atemt)
if atemt==0:
    print("Access Denied😒")
    print("Press enter to open it after 30 sec")
    input()