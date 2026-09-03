# Task Tracker CLI

A simple command-line task tracker built with **Python** and **JSON**.

The application allows users to create, update, delete, and manage tasks directly from the command line. Tasks are stored persistently in a `tasks.json` file.

## Features

* Add new tasks
* Update existing tasks
* Delete tasks
* Mark tasks as `todo`
* Mark tasks as `in-progress`
* Mark tasks as `done`
* List all tasks
* List tasks by status
* Automatically generate unique task IDs
* Store tasks in a JSON file
* Automatically create the task storage when needed
* Track task creation and update timestamps
* Handle invalid commands and task IDs

## Technologies Used

* Python 3
* JSON
* Python Standard Library

  * `json`
  * `datetime`
  * `os`
  * `sys`

No external libraries or frameworks are required.

## Project Structure

```text
task-tracker/
│
├── task_cli.py
├── tasks.json
└── README.md
```

`tasks.json` is created automatically when tasks are added.

## Requirements

You need:

* Python 3.x
* A terminal or command prompt

Check your Python installation with:

```bash
python --version
```

## Usage

Run the application using:

```bash
python task_cli.py <command>
```

### Add a Task

```bash
python task_cli.py add "Buy groceries"
```

Example output:

```text
Task added successfully (ID: 1)
```

### List All Tasks

```bash
python task_cli.py list
```

Example:

```text
1. Buy groceries [todo]
2. Learn Python [done]
3. Practice DSA [in-progress]
```

### Update a Task

```bash
python task_cli.py update 1 "Buy groceries and cook dinner"
```

Example output:

```text
Task updated successfully.
```

### Delete a Task

```bash
python task_cli.py delete 1
```

Example output:

```text
Task deleted successfully.
```

### Mark a Task as In Progress

```bash
python task_cli.py mark-in-progress 1
```

Example output:

```text
Task marked as in-progress.
```

### Mark a Task as Done

```bash
python task_cli.py mark-done 1
```

Example output:

```text
Task marked as done.
```

## Listing Tasks by Status

### Todo Tasks

```bash
python task_cli.py list todo
```

### In-Progress Tasks

```bash
python task_cli.py list in-progress
```

### Completed Tasks

```bash
python task_cli.py list done
```

## Task Format

Each task is stored in `tasks.json` using the following structure:

```json
{
    "id": 1,
    "description": "Learn Python",
    "status": "todo",
    "createdAt": "2026-09-03T12:30:00",
    "updatedAt": "2026-09-03T12:30:00"
}
```

### Task Properties

| Property      | Description                                  |
| ------------- | -------------------------------------------- |
| `id`          | Unique identifier for the task               |
| `description` | Description of the task                      |
| `status`      | Current task status                          |
| `createdAt`   | Date and time when the task was created      |
| `updatedAt`   | Date and time when the task was last updated |

Valid statuses are:

```text
todo
in-progress
done
```

## Error Handling

The application handles common errors such as:

* Missing command arguments
* Invalid task IDs
* Non-numeric task IDs
* Unknown commands
* Invalid task statuses
* Missing or invalid JSON files

For example:

```bash
python task_cli.py delete 999
```

If the task doesn't exist:

```text
Task not found.
```

## How It Works

The application uses Python's `sys.argv` to read positional command-line arguments.

For example:

```bash
python task_cli.py add "Learn Python"
```

is received by Python approximately as:

```python
[
    "task_cli.py",
    "add",
    "Learn Python"
]
```

The program then determines which command was entered and calls the appropriate function.

Tasks are loaded from `tasks.json`, modified in memory, and then written back to the JSON file.

## Learning Objectives

This project was built to practice:

* Python functions
* Lists and dictionaries
* File handling
* JSON serialization and deserialization
* Command-line arguments
* `sys.argv`
* Exception handling
* Input validation
* Date and time handling
* CRUD operations
* Searching and modifying data
* Basic application structure

## Future Improvements

Possible future improvements include:

* Add task priorities
* Add due dates
* Add search functionality
* Add sorting by creation date or status
* Add colored terminal output
* Add automated tests
* Refactor the CLI into separate modules
* Replace JSON storage with a SQL database
* Build a REST API using a Python web framework

## Author

Built as a Python programming project to practice command-line applications, file handling, JSON persistence, and application design.
