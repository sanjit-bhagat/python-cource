                                                            # LOGIN & REGISTRATION SYSTEM.

File_name="login.txt"

def register():
    Username=input("Enter New Username=")
    Password=input("Enter New Password=")

    try:
        with open(File_name,  "r")as file:
            for line in file:
                saved_username,_=line.strip().split(",")
                if saved_username==Username:
                    print("username already exists.")
                    return
    except FileNotFoundError:
        pass

    with open(File_name,  "a")as file:
        file.write(f"{Username},{Password}\n")
        
        print("Register Sucessfully.")

def Login():
    username=input("Enter Username=")
    password=input("Enter Password=")
    found=False

    try:
        with open(File_name,  "r")as file:
            for line in file:
                saved_username,saved_password=line.strip().split(",")
                if saved_username==username and saved_password==password:
                    print("Login sucessfully.")
                    found=True
                    return
            if not found:
                print("Invalid username and password.")
        
    except FileNotFoundError:
        print("No user register yet.")

def main():
    while True:

        print("|---- LOGIN AND REGISTER----|")
        print("1. Register")
        print("2. Login")
        print("3. Exit")

        choice=input("Enter Your Choice=")

        if choice=='1':
            register()

        elif choice=='2':
            Login()

        elif choice=='3':
            print("Existing System")
            break
        else:
            print("Invalid choice plx try Again.")

main()

