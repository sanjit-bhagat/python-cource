                        # simple Student Marks Managements system

def Add_marks():
    m=int(input("Add marks:"))
    marks.append(m)

def View_Marks():
    if marks==[]:
        print("Add marks first")
    else:
        print("marks:", marks)

def high_low():
    print("highest marks:", max(marks))
    print("Lowest marks:", min(marks))

def  Average():
    avg=sum(marks)/len(marks)
    print("Average of marks is:", avg)

def Exit():
    print("thanks for using this system, visit again.")
marks=[]
while True:

    print("1. Add Mask")
    print("2. View Mask")
    print("3. highest and lowest")
    print("4. Average ")
    print("5. Exit")

    choice=int(input("Enter your choice:"))

    if choice==1:
        Add_marks()

    elif choice==2:
        View_Marks()
        
    elif choice==3:
        high_low()

    elif choice==4:
        Average()

    elif choice==5:
        Exit()
        break

    else:
        print("Invalid choice.")




