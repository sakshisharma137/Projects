username="Sakshi"
pin=1234
balance=5000

name=(input("Enter User_Name: "))


if (name==username):
    Pin=int(input("Enter Pin: "))
    if Pin==pin:
        while True:    
            print("Menu \n 1. Check Balance \n 2. Deposit \n 3. Withdraw \n 4. Exit")
    
    
            choice=int(input("Enter choice(1-3)"))
        
            if choice==1:

                print("Total Balance=",balance)
            elif(choice==2):
                deposit=int(input("Enter Amount:"))
                balance +=deposit
                print("After Depoisit: ",balance)
            elif(choice==3):
                withdraw=int(input("Enter Amount to Withdrawl:"))
                if(balance>withdraw):
                    balance-=withdraw
                    print("After withdraw Current Balance=",balance)
       
                else:
                    print("Not sufficient balance")
            elif(choice==4):
                print("Thankyou For using ATM")
                break
            else:
                print("Enter valid choice")
                
                    
    else:
            print("Invalid pin")
else:
    print("invalid Username")