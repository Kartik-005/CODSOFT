# TASK 1 - TO-DO LIST APPLICATION
# A simple command-line to-do list where the user can
# add, view, update, and delete tasks.

tasks = []

def show_menu():
    print("\n----- TO-DO LIST MENU -----")
    print("1. View tasks")
    print("2. Add a task")
    print("3. Mark a task as done")
    print("4. Delete a task")
    print("5. Exit")

def view_tasks():
    if len(tasks) == 0:
        print("\nYour to-do list is empty!")
    else:
        print("\nYour Tasks:")
        for i in range(len(tasks)):
            status = "Done" if tasks[i]["done"] else "Not done"
            print(str(i + 1) + ". " + tasks[i]["name"] + " [" + status + "]")

def add_task():
    task_name = input("Enter the new task: ")
    tasks.append({"name": task_name, "done": False})
    print("Task added successfully!")

def mark_done():
    view_tasks()
    if len(tasks) == 0:
        return
    choice = int(input("Enter the task number to mark as done: "))
    if 1 <= choice <= len(tasks):
        tasks[choice - 1]["done"] = True
        print("Task marked as done!")
    else:
        print("Invalid task number.")

def delete_task():
    view_tasks()
    if len(tasks) == 0:
        return
    choice = int(input("Enter the task number to delete: "))
    if 1 <= choice <= len(tasks):
        removed = tasks.pop(choice - 1)
        print("Deleted task:", removed["name"])
    else:
        print("Invalid task number.")

# Main program loop
while True:
    show_menu()
    option = input("Choose an option (1-5): ")

    if option == "1":
        view_tasks()
    elif option == "2":
        add_task()
    elif option == "3":
        mark_done()
    elif option == "4":
        delete_task()
    elif option == "5":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")
