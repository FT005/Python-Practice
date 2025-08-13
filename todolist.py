tasks = []

print("Welcome to Your To-Do List Manager!")

while True:
    print("\nMenu:")
    print("1. Add a task")
    print("2. View tasks")
    print("3. Remove a task")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == '1':
        task = input("Enter the task: ")
        tasks.append(task)
        print(f"Task '{task}' added.")
    elif choice == '2':
        if tasks:
            print("Your tasks:")
            for i, t in enumerate(tasks, start=1):
                print(f"{i}. {t}")
        else:
            print("No tasks added yet.")
    elif choice == '3':
        if tasks:
            print("Which task number do you want to remove?")
            for i, t in enumerate(tasks, start=1):
                print(f"{i}. {t}")
            task_num = int(input("Enter number: "))
            if 1 <= task_num <= len(tasks):
                removed = tasks.pop(task_num - 1)
                print(f"Task '{removed}' removed.")
            else:
                print("Invalid task number.")
        else:
            print("No tasks to remove.")
    elif choice == '4':
        print("Exiting To-Do List Manager. Goodbye!")
        break
    else:
        print("Invalid choice, please try again.")
