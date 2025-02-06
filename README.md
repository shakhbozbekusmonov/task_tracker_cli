# Task Tracker CLI

A simple command-line interface (CLI) application for managing a task list. This CLI allows users to create, update, delete, and list tasks with various statuses (todo, in-progress, done).

Features
- Add new tasks
- Update task descriptions
- Mark tasks as in-progress or done
- List tasks by status
- Delete tasks by ID

Prerequisites
- Python 3.6 or higher
-  click module (pip install click)

Installation
1. Clone the repository:
```
git clone git@github.com:shakhbozbekusmonov/task_tracker_cli.git 
cd task_tracker_cli
```

2. Install dependencies:
```
pip install click
```


Usage
1. Run the CLI:
```
python task_cli.py
```
2. Available commands:
- Add a new task
```
python task_cli.py add "Your task description"
```

Example:
```
python task_cli.py add "Finish the project documentation"
```
- List all tasks or tasks with a specific status (todo, in-progress, done)

```
python task_cli.py list
python task_cli.py list todo
```

- Update a task’s description
```
python task_cli.py update <task_id> "New task description"
```

Example:
```
python task_cli.py update 1 "Submit the project"
```

- Mark a task as in-progress
```
python task_cli.py mark_in_progress <task_id>
```

Example:
```
python task_cli.py mark_in_progress 2
```

- Mark a task as done
```
python task_cli.py mark_done <task_id>
```

Example:
```
python task_cli.py mark_done 2
```

- Delete a task
```
python task_cli.py delete <task_id>
```

Example:
```
python task_cli.py delete 3
```


Project Page

Visit the project page at: https://github.com/shakhbozbekusmonov/task_tracker_cli.git
