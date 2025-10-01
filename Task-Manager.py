import json
import os

FILE = os.path.join(os.path.dirname(__file__), "tasks.json")


def load_tasks():
    try:
        with open(FILE, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return []

def save_tasks(tasks):
    with open(FILE, "w") as f:
        json.dump(tasks, f, indent=4)

def add_task(task):
    tasks = load_tasks()
    tasks.append({"laundry": task, "done": False})
    save_tasks(tasks)
    print(f"✅ Task added: {task}")

def list_tasks():
    tasks = load_tasks()
    if not tasks:
        print("📭 No tasks found.")
    else:
        for i, t in enumerate(tasks, start=1):
            status = "✔" if t["done"] else "❌"
            print(f"{i}. {t['task']} [{status}]")

def mark_done(task_number):
    tasks = load_tasks()
    if 1 <= task_number <= len(tasks):
        tasks[task_number - 1]["done"] = True
        save_tasks(tasks)
        print(f"✔ Task marked as done: {tasks[task_number - 1]['task']}")
    else:
        print("⚠ Invalid task number")


if __name__ == "__main__":
    while True:
        print("\n--- Task Manager ---")
        print("1. Add Task")
        print("2. List Tasks")
        print("3. Mark Task as Done")
        print("4. Exit")
        choice = input("Choose: ")

        if choice == "1":
            task = input("Enter task: ")
            add_task(task)
        elif choice == "2":
            list_tasks()
        elif choice == "3":
            list_tasks()
            num = int(input("Enter task number to mark as done: "))
            mark_done(num)
        elif choice == "4":
            print("👋 Goodbye!")
            break  
        else:
            print("⚠ Invalid option")

