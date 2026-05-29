#Create a simple ATM program that allows users to:
'''Check balance - print the balance 
Deposit money - take user input for how mush money they want to  deposite and while fetching total balance this mst be shown 
Withdraw money- this amount must be dedeucted while showing the final balance 
Exit the program
Conditions:
Initial balance should be predefined
Prevent withdrawal if balance is low
Use menu-driven approach'''
Initial_balance=120000
while True:
    print("------Menu------")
    print("1. Deposit money \n 2.Withdraw money \n 3. Check Balance \n 4.Exit the program ")
    choice = int(input("Enter your choice: "))
    match choice:
        case 1 :
            deposit_money = int(input("Enter the deposite money"))
            Initial_balance += deposit_money
            print("Money Deposited")
            input()
        case 2 :
            withdraw_money = int(input ("Enter the amount to withdraw: "))
            if Initial_balance>withdraw_money:
                Initial_balance -= withdraw_money
                print("Money is withdrawed ")
                input("Press Enter to Continue")
            else:
                print("Insufficient balance ")
                input("Press Enter to Continue")
        case 3 :
            print("Total balance = ",Initial_balance)
            input("Press Enter to Continue")
        case 4 :
            print("Program exited. ")
            input("Press Enter to Continue")
            break
        case _ :
            print("Invalid choice") 
            input("Press Enter to Continue")              
