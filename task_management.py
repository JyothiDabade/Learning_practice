import os

# ---------- Helper Functions ----------

def user_file(username):
    return username + "_tasks.txt"


# ---------- Authentication ----------

def register():
    print("\n--- Register ---")
    username = input("Create username: ")

    # Check if username already exists
    if os.path.exists("users.txt"):
        with open("users.txt", "r") as f:
            for line in f:
                if username == line.strip().split(",")[0]:
                    print("Username already exists!")
                    return None

    password = input("Create password: ")

    # Save username and password in plain text
    with open("users.txt", "a") as f:
        f.write(username + "," + password + "\n")

    print("Registration successful!")
    return username


def login():
    print("\n--- Login ---")
    username = input("Username: ")
    password = input("Password: ")

    if not os.path.exists("users.txt"):
        print("No users registered yet!")
        return None

    with open("users.txt", "r") as f:
        for line in f:
            stored_user, stored_pass = line.strip().split(",")
            if stored_user == username and stored_pass == password:
                print("Login successful!")
                return username

    print("Invalid username or password!")
    return None


# ---------- Task Functions ----------

def add_task(username):
    task = input("Enter task: ")
    with open(user_file(username), "a") as f:
        f.write(task + ",Pending\n")
    print("Task added.")


def view_tasks(username):
    print("\n--- Your Tasks ---")
    if not os.path.exists(user_file(username)):
        print("No tasks yet.")
        return

    with open(user_file(username), "r") as f:
        tasks = f.readlines()

    for i, t in enumerate(tasks, 1):
        task, status = t.strip().split(",")
        print(f"{i}. {task} [{status}]")


def mark_completed(username):
    view_tasks(username)
    if not os.path.exists(user_file(username)):
        return
    num = int(input("Enter task number to complete: "))

    with open(user_file(username), "r") as f:
        tasks = f.readlines()

    if 1 <= num <= len(tasks):
        task, _ = tasks[num - 1].strip().split(",")
        tasks[num - 1] = task + ",Completed\n"

        with open(user_file(username), "w") as f:
            f.writelines(tasks)

        print("Task marked as completed.")
    else:
        print("Invalid task number.")


def delete_task(username):
    view_tasks(username)
    if not os.path.exists(user_file(username)):
        return
    num = int(input("Enter task number to delete: "))

    with open(user_file(username), "r") as f:
        tasks = f.readlines()

    if 1 <= num <= len(tasks):
        tasks.pop(num - 1)

        with open(user_file(username), "w") as f:
            f.writelines(tasks)

        print("Task deleted.")
    else:
        print("Invalid task number.")


# ---------- Main Menu ----------

def task_menu(username):
    while True:
        print(f"\n--- Task Menu ({username}) ---")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Complete Task")
        print("4. Delete Task")
        print("5. Logout")

        choice = input("Choose option: ")

        if choice == "1":
            add_task(username)
        elif choice == "2":
            view_tasks(username)
        elif choice == "3":
            mark_completed(username)
        elif choice == "4":
            delete_task(username)
        elif choice == "5":
            print("Logging out...")
            break
        else:
            print("Invalid option!")


def main():
    while True:
        print("\n--- Task Manager ---")
        print("1. Login")
        print("2. Register")
        print("3. Exit")

        choice = input("Choose option: ")

        if choice == "1":
            user = login()
            if user:
                task_menu(user)
        elif choice == "2":
            user = register()
            if user:
                task_menu(user)
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid option!")


# Run the program
main()
