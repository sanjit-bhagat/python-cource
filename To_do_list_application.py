# To Do List Application      simple
Tasks=[]

def Add_Task():
    new_task=input("Enter New Task:")
    Tasks.append(new_task)
    if new_task in Tasks:
        print("Task is Added.")

def View_Task():
    if not Tasks:
        print("Task is not Available.")
    else:
        print("Your Task")
        for i, task in enumerate(Tasks, start=1):
            print(i, task)

def Remove_task():
    View_Task()
    num=int(input("Enter the no of Task is remove:"))
    if Tasks.pop(num-1):
        print("Task Remove sucessfully.")
    else:
        print("Add Task first.")
    
def Exit():
    print("Thanks for Using Application.")
    
while True:
    print("Choose the Below Option.")
    print("1.  Add_Task")
    print("2.  View_Task")
    print("3.  Remove_Task")
    print("4.  Exit ")

    choice=int(input("Enter Your Choice:"))

    if choice==1:
        Add_Task()
    elif choice==2:
        View_Task()
    elif choice==3:
        Remove_task()
    elif choice==4:
        Exit()
        break
    else:

        print("Invalid Input.")

