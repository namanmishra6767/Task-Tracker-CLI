import sys
import json
from datetime import datetime
import os


FILE_NAME = "tasks.json"

def load_tasks():
    """Load tasks from the JSON file."""

    if not os.path.exists(FILE_NAME):
        return []

    try:
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    except (json.JSONDecodeError, OSError):
        return []


def save_tasks(tasks):
    """Save tasks to the JSON file."""

    try:
        with open(FILE_NAME, "w") as file:
            json.dump(tasks, file, indent=4)
    except OSError:
        print("Error: Could not save tasks.")


# =========================
# HELPER FUNCTIONS
# =========================

def get_timestamp():
    """Return the current date and time."""

    return datetime.now().isoformat(timespec="seconds")


def get_next_id(tasks):
    """Generate the next unique task ID."""

    if not tasks:
        return 1

    return max(task["id"] for task in tasks) + 1


def find_task(tasks, task_id):
    """Find a task by ID."""

    for task in tasks:
        if task["id"] == task_id:
            return task

    return None


# =========================
# ADD TASK
# =========================

def add_task(description):
    tasks = load_tasks()

    timestamp = get_timestamp()

    task = {
        "id": get_next_id(tasks),
        "description": description,
        "status": "todo",
        "createdAt": timestamp,
        "updatedAt": timestamp
    }

    tasks.append(task)
    save_tasks(tasks)

    print(f"Task added successfully (ID: {task['id']})")


# =========================
# UPDATE TASK
# =========================

def update_task(task_id, description):
    tasks = load_tasks()

    task = find_task(tasks, task_id)

    if task is None:
        print("Task not found.")
        return

    task["description"] = description
    task["updatedAt"] = get_timestamp()

    save_tasks(tasks)

    print("Task updated successfully.")


# =========================
# DELETE TASK
# =========================

def delete_task(task_id):
    tasks = load_tasks()

    task = find_task(tasks, task_id)

    if task is None:
        print("Task not found.")
        return

    tasks.remove(task)

    save_tasks(tasks)

    print("Task deleted successfully.")


# =========================
# MARK IN PROGRESS
# =========================

def mark_in_progress(task_id):
    tasks = load_tasks()

    task = find_task(tasks, task_id)

    if task is None:
        print("Task not found.")
        return

    task["status"] = "in-progress"
    task["updatedAt"] = get_timestamp()

    save_tasks(tasks)

    print("Task marked as in-progress.")


# =========================
# MARK DONE
# =========================

def mark_done(task_id):
    tasks = load_tasks()

    task = find_task(tasks, task_id)

    if task is None:
        print("Task not found.")
        return

    task["status"] = "done"
    task["updatedAt"] = get_timestamp()

    save_tasks(tasks)

    print("Task marked as done.")


# =========================
# LIST TASKS
# =========================

def list_tasks(status=None):
    tasks = load_tasks()

    if status is not None:
        tasks = [
            task for task in tasks
            if task["status"] == status
        ]

    if not tasks:
        print("No tasks found.")
        return

    for task in tasks:
        print(
            f"{task['id']}. "
            f"{task['description']} "
            f"[{task['status']}]"
        )


# =========================
# COMMAND LINE HANDLING
# =========================

def main():

    if len(sys.argv) < 2:
        print("Usage:")
        print('  python task_cli.py add "Task description"')
        print('  python task_cli.py update <id> "New description"')
        print("  python task_cli.py delete <id>")
        print("  python task_cli.py mark-in-progress <id>")
        print("  python task_cli.py mark-done <id>")
        print("  python task_cli.py list")
        print("  python task_cli.py list done")
        print("  python task_cli.py list todo")
        print("  python task_cli.py list in-progress")
        return

    command = sys.argv[1]

    # ADD
    if command == "add":

        if len(sys.argv) < 3:
            print("Error: Please provide a task description.")
            return

        description = sys.argv[2]
        add_task(description)

    # UPDATE
    elif command == "update":

        if len(sys.argv) < 4:
            print("Usage: python task_cli.py update <id> \"New description\"")
            return

        try:
            task_id = int(sys.argv[2])
        except ValueError:
            print("Error: Task ID must be a number.")
            return

        description = sys.argv[3]

        update_task(task_id, description)

    # DELETE
    elif command == "delete":

        if len(sys.argv) < 3:
            print("Error: Please provide a task ID.")
            return

        try:
            task_id = int(sys.argv[2])
        except ValueError:
            print("Error: Task ID must be a number.")
            return

        delete_task(task_id)

    # MARK IN PROGRESS
    elif command == "mark-in-progress":

        if len(sys.argv) < 3:
            print("Error: Please provide a task ID.")
            return

        try:
            task_id = int(sys.argv[2])
        except ValueError:
            print("Error: Task ID must be a number.")
            return

        mark_in_progress(task_id)

    # MARK DONE
    elif command == "mark-done":

        if len(sys.argv) < 3:
            print("Error: Please provide a task ID.")
            return

        try:
            task_id = int(sys.argv[2])
        except ValueError:
            print("Error: Task ID must be a number.")
            return

        mark_done(task_id)

    # LIST
    elif command == "list":

        if len(sys.argv) == 2:
            list_tasks()

        elif len(sys.argv) == 3:

            status = sys.argv[2]

            if status not in ["done", "todo", "in-progress"]:
                print("Error: Invalid status.")
                print("Use: done, todo, or in-progress")
                return

            list_tasks(status)

        else:
            print("Error: Invalid list command.")

    else:
        print(f"Error: Unknown command '{command}'.")



if __name__ == "__main__":
    main()