                                          # FILE HANDLING, STUDENT RECORDS.

file_name="student.txt"

def add_student():
    roll=input("Enter roll number=")
    Name=input("Enter name  of Student=")
    Marks=input("Enter marks  of Student=")

    with open(file_name,  "a") as file:
        file.write(f"{roll}, {Name}, {Marks}\n")

    print("student Added sucessfully.")

def view_student():
    try:
        with open(file_name,  "r")as file:
            print("Student Records.")
            for line in file:
                roll, Name, Marks=line.strip().split(",")
                print(f"roll_no={roll}, Name={Name}, Marks={Marks}")
    
    except FileNotFoundError:
        print("No record found.")

def search_student():
    search_roll=input("Search your Roll number=")
    found=False

    try:
        with open(file_name,  "r")as file:
            for line in file:
                roll, Name, Marks=line.strip().split(",")
                if roll==search_roll:
                    print("Record Found")
                    print(f"roll={roll}, Name={Name}, Marks={Marks}")
                    found=True
                    break
        if not found: 
            print("Student not found")
    except FileNotFoundError:
        print("file not found")

def main():
    while True:
        print("|---- STUDENT RECORDS ----|")
        print("1. Add Student.")
        print("2. View Student.")
        print("3. Search Student.")
        print("4. Exit.")

        choice=int(input("Enter your choice="))

        if choice==1:
            add_student()
        
        elif choice==2:
            view_student()

        elif choice==3:
            search_student()

        elif choice==4:
            print("Existing the system.")
            break
        else:
            print("Invalid Choice plz, try Again.")
main()

        




