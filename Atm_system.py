                # Full ATM Function 

class Account1:
    def __init__(self, acc_no, name,pin):
        self.acc_no=acc_no
        self.name=name
        self.pin=pin
        self.balance=0

    def deposite(self, amount):
        self.balance+=amount
        print(f"{amount}Rs is deposite Sucessfully.")

    def withdraw(self, amount):
        if amount>self.balance:
            print("Insufficent Amount.")
        else:
            self.balance-=amount
            print(f"{amount}Rs is withdraw sucessfully.")

    def Check_balance(self):
        print(f"Account: {self.acc_no}")
        print(f"Nmae: {self.name}")
        print(f"Balance: Rs.{self.balance}")
        print("------------------------")


# main program 

Account={ }
while True:
    print("/-- ATM System --/")
    print("1. Create Account")
    print("2. Login Account")
    print("3. Exit")

    choice=input("Enter Your Choice=")
    
    #Create Account.
    if choice=='1':
        acc_no=input("Enter Account Number :")
        name=input("Enter your name :")
        pin=input("Set  4 digit Pin :")

        Account[acc_no]=Account1(acc_no, name, pin)
        print("Account created sucessfully ")

    #login
    elif choice=='2':
        acc_no=input("Enter Account Number:")

        if acc_no in Account:
            pin=input("Enetr Pin:")

            if pin==Account[acc_no].pin:
                print("Login Sucessfully")


                # Main
                while True:
                    print("---- ATM MENU----")
                    print("1. Deposite")
                    print("2. Withdraw")
                    print("3. Check Balance")
                    print("4. Logout")

                    main_choice=input("Enter Your choice=")

                    if main_choice=='1':
                        amt=int(input("Enter Amount to Deposite: "))
                        Account[acc_no].deposite(amt)

                    elif main_choice=='2':
                        amt=int(input("Enter Amount to withdraw: "))
                        Account[acc_no].withdraw(amt)

                    elif main_choice=='3':
                        Account[acc_no].Check_balance()

                    elif main_choice=='4':
                        print("Logout sucessfully")
                        break

                    else:
                        print("Invalid choice! please Try Again.")

                else:
                    print("Incorrect Pin.")

            else:
                print("Account is not found.")


        elif choice=='3':
            print("Thanks for Using ATM")
            break

        else:
            print("Please Try again.")










        