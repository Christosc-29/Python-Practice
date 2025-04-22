FILENAME = "taskks.txt"
def add_task():
    title = input("Enter task name: ")
    details = input("Enter task details: ")
    with open(FILENAME, "a") as file:
        file.write(title + " ::: " + details + "\n")
    print("Task added!\n")

def show_tasks():
    try:
        with open(FILENAME, "r") as file:
            lines = file.readlines()
            if len(lines) == 0:
                print("No tasks found.\n")
                return
            for i in range(len(lines)):
                task_line = lines[i]
                task_name = task_line.split(" ::: ")[0]
                print(f"{i+1}. {task_name}")
            print()
    except FileNotFoundError:
        print("No tasks file found.\n")

def show_task_details():
    try:
        with open(FILENAME, "r") as file:
            lines = file.readlines()
            task_num = int(input("Enter task number to view details: "))
            if 1 <= task_num <= len(lines):
                task_line = lines[task_num - 1]
                task_name, task_details = task_line.split(" ::: ")
                print("\nTask:", task_name)
                print("Details:", task_details.strip(), "\n")
            else:
                print("Task number does not exist.\n")
    except:
        print("Something went wrong or task file not found.\n")

def delete_task():
    try:
        with open(FILENAME, "r") as file:
            lines = file.readlines()
        task_num = int(input("Enter task number to delete: "))
        if 1 <= task_num <= len(lines):
            task_line = lines[task_num - 1]
            task_name = task_line.split(" ::: ")[0]
            confirm = input(f"Are you sure you want to delete task '{task_name}'? (Y/N): ").lower()
            if confirm == "y":
                lines.pop(task_num - 1)
                with open(FILENAME, "w") as file:
                    file.writelines(lines)
                print("Task deleted!\n")
            else:
                print("Delete cancelled.\n")
        else:
            print("Task number does not exist.\n")
    except:
        print("Something went wrong.\n")

def menu():
    while True:
        print("----- TASK MANAGER -----")
        print("1. Add Task")
        print("2. Show All Tasks")
        print("3. View Task Details")
        print("4. Delete Task")
        print("5. Exit")
        choice = input("Choose an option: ")
        print()

        if choice == "1":
            add_task()
        elif choice == "2":
            show_tasks()
        elif choice == "3":
            show_task_details()
        elif choice == "4":
            delete_task()
        elif choice == "5":
            break
        else:
            print("Invalid option. Try again.\n")

menu()
