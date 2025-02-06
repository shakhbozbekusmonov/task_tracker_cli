import datetime
import click
import json
from pathlib import Path


TASK_FILE = Path("tasks.json")


def load_tasks():
    """Load tasks from file"""
    if TASK_FILE.exists():
        with open(TASK_FILE, "r") as file:
            return json.load(file)
    return []


def save_tasks(todos):
    """Save tasks to file"""
    with open(TASK_FILE, "w") as file:
        json.dump(todos, file)


@click.group()
def cli():
    """Task List CLI"""
    pass


@cli.command()
@click.argument('task')
def add(task):
    """Add a new task"""
    try:
        tasks = load_tasks()
        new_task = {
            "id": len(tasks) + 1,
            "description": task,
            "status": "todo",
            "createdAt": str(datetime.datetime.now()),
            "updatedAt": str(datetime.datetime.now())
        }
        tasks.append(new_task)
        save_tasks(tasks)
        click.echo(f"Task added successfully (ID: {len(tasks)})")
    except Exception as e:
        click.echo(f"Error: {e}")

@cli.command()
@click.argument('task_id', type=int)
@click.argument("description", type=str)
def update(task_id, description):
    """Update a task"""
    try:
        tasks = load_tasks()
        for task in tasks:
            if task['id'] == task_id:
                task['description'] = description
                task["updatedAt"] = str(datetime.datetime.now())
        save_tasks(tasks)
        click.echo("Successfully updated task")
    except IndexError:
        click.echo("Task not found")


@cli.command()
@click.argument("task_id", type=int)
def delete(task_id):
    """Delete a task by ID"""
    try:
        tasks = load_tasks()
        task_to_delete = None

        for task in tasks:
            if task["id"] == task_id:
                task_to_delete = task
                break

        if task_to_delete:
            tasks.remove(task_to_delete)
            save_tasks(tasks)
            click.echo(f"Successfully deleted task {task_id}")
        else:
            click.echo(f"Task with ID {task_id} not found.")
    except Exception as e:
        click.echo(f"An error occurred: {e}")


@cli.command()
@click.argument("task_id", type=int)
def mark_in_progress(task_id):
    """Mark a task as in progress"""
    try:
        tasks = load_tasks()
        for task in tasks:
            if task['id'] == task_id:
                task["status"] = "in-progress"
                task["updatedAt"] = str(datetime.datetime.now())
        save_tasks(tasks)
        click.echo("Successfully marked task as in progress")
    except IndexError:
        click.echo("Task not found")

@cli.command()
@click.argument("task_id", type=int)
def mark_done(task_id):
    """Mark a task as done"""
    try:
        tasks = load_tasks()
        for task in tasks:
            if task["id"] == task_id:
                task["status"] = "done"
                task["updatedAt"] = str(datetime.datetime.now())
        save_tasks(tasks)
        click.echo("Successfully marked task as done")
    except IndexError:
        click.echo("Task not found")

@cli.command()
@click.argument("status", required=False)
def list(status):
    try:
        tasks = load_tasks()

        if not tasks:
            click.echo("Task not found")
            return
        filtered_tasks = [task for task in tasks if status is None or task['status'] == status]
        if not filtered_tasks:
            click.echo(f"'{status}' tasks not found")
        else:
            for task in filtered_tasks:
                click.echo(f"{task['id']}: {task['description']} [{task['status']}]")
    except Exception as e:
        click.echo(f"Error: {e}")

if __name__ == '__main__':
    cli()
