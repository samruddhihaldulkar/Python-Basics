cp="Samruddhi@12"
cun="Samruddhihaldulkar"
atemt=5
while atemt>0:
    np=input("Enter new password: ")
    nun=input("Enter new username: ")
    if cp==np and cun==nun:
        print("Access gained✅")
        break
    else:
        print("Wrong username or Password❌")
        atemt-=1
        print("Attempts left = ",atemt) 
if atemt==0:
    print("Access Denied😒")           