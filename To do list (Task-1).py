tasks = []
def show_menu():
    print("\n --- TO-DO LIST MENU ---")
    print("1.Add task")
    print("2.View tasks")
    print("3.Delete task")
    print("4.Exit")

def add_task():
    task=input("Enter your task:")
    tasks.append(task)
    print("Task added successfully!")

def view_tasks():
    if not tasks:
        print("No tasks found")
    else:
        print("\nYour tasks:")
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")

def delete_task():
    view_tasks()
    try:
        task_num=int(input("Enter task number to delete:"))
        if 1<=task_num<=len(tasks):
            removed=tasks.pop(task_num-1)
            print(f"Task '{removed}' deleted")
        else:
            print("Invalid task number")
    except ValueError:
        print("Please enter a valid number")
while True:
    show_menu()
    choice=input("Enter your choice: ")

    if choice=='1':
        add_task()
    elif choice=='2':
        view_tasks()
    elif choice=='3':
        delete_task()
    elif choice=='4':
        print("Exiting... goodbye!")
        break
    else:
        print("Invalid choice ,try again")