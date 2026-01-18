# Simple To-Do List Program
# Created for CodSoft Python Programming Internship
# Author: Revathi R

todo_tasks = []

def display_menu():
    print("\n===== MY TO-DO LIST =====")
    print("1. Add a new task")
    print("2. View all tasks")
    print("3. Delete a task")
    print("4. Exit")

def add_new_task():
    task = input("Enter a new task: ")
    todo_tasks.append(task)
    print("Task added successfully!")
    print(f"Total tasks now: {len(todo_tasks)}")

def show_tasks():
    if len(todo_tasks) == 0:
        print("Your to-do list is empty.")
    else:
        print("\nYour Tasks:")
        for index, task in enumerate(todo_tasks, start=1):
            print(f"{index}. {task}")

def delete_task():
    show_tasks()
    if len(todo_tasks) == 0:
        return
    try:
        choice = int(input("Enter task number to delete: "))
        if 1 <= choice <= len(todo_tasks):
            removed_task = todo_tasks.pop(choice - 1)
            print(f"Deleted task: {removed_task}")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter numbers only.")

while True:
    display_menu()
    user_choice = input("Choose an option (1-4): ")

    if user_choice == "1":
        add_new_task()
    elif user_choice == "2":
        show_tasks()
    elif user_choice == "3":
        delete_task()
    elif user_choice == "4":
        print("Thank you for using the To-Do List. Goodbye!")
        break
    else:
        print("Invalid option. Please try again.")
