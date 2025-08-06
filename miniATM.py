correct_pin= 1234
balance= 5000
pin = int(input("Enter for 4 digit pin"))
if pin == correct_pin:
    print("Welcome to the ATM")
    print("1. Check Balance")
    print("2. Withdraw amount")
    print("3. Exit")

    choice=int(input("Enter your choice"))
    if choice==1:
        print("Your total balance is ",balance)

    elif choice==2:
        amt=int(input("Enter the amount"))
        balance = balance-amt
        if amt<=balance:
            print("please collect your cash")
            print("Your remaining balance is ",balance)
        else:
            print("Insufficient balance")
    
    elif choice==3:
        print("Thanks for visiting")

    else:
        print("Invalid options")
    
else:
    print("You have entered the wrong PIN. Please try again later.")