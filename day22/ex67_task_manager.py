import time

# List that stores all tasks
tasks = []


# Function to add a new task
def add_task():
    task_name = input("Enter the task name: ").lower()
    priority = int(input("Enter priority (1 = highest, 5 = lowest): "))

    time.sleep(1)

    task = {
        "task": task_name,
        "priority": priority
    }

    tasks.append(task)

    print("Task created successfully.")


# Function to delete a task
def delete_task():

    if tasks:
        task_name = input("Enter the task you want to remove: ").lower()

        for task in tasks:
            if task["task"] == task_name:
                tasks.remove(task)
                time.sleep(1)
                print("Task removed successfully.")
                return

        print("Task not found.")

    else:
        print("No tasks registered.")


# Function to update task priority
def update_task():

    if tasks:
        task_name = input("Enter the task you want to update: ").lower()

        for task in tasks:
            if task["task"] == task_name:
                priority = int(input("Enter new priority (1-5): "))
                task["priority"] = priority
                print("Task updated successfully.")
                return

        print("Task not found.")

    else:
        print("No tasks registered.")


# Function to display all tasks
def show_tasks():

    if tasks:
        print("\nLoading tasks...")
        time.sleep(1)

        for i, task in enumerate(tasks, start=1):
            print(f"{i}. Task: {task['task']} | Priority: {task['priority']}")

    else:
        print("No tasks registered.")


# Function to display the menu
def menu():

    print("\n" + "=" * 40)
    print("TASK MANAGER")
    print("=" * 40)
    print("1 - Add Task")
    print("2 - Remove Task")
    print("3 - Update Task Priority")
    print("4 - Show Tasks")
    print("5 - Exit")
    print("=" * 40)


# Dictionary that maps menu options to functions
options = {
    1: add_task,
    2: delete_task,
    3: update_task,
    4: show_tasks,
}


# Function that validates and executes menu options
def valid_option(menu_choice):

    if menu_choice in options:
        options[menu_choice]()
    else:
        print("Please choose a valid option.")


# Main program loop
while True:

    menu()

    try:
        menu_choice = int(input("Choose an option: "))

        if menu_choice == 5:
            print("Goodbye.")
            break

        valid_option(menu_choice)

    except ValueError:
        print("Please enter a number.")
    