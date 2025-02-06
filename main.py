import click
import json
from pathlib import Path

# Fayl yo‘li
TODO_FILE = Path("todos.json")

# Fayldan vazifalarni o‘qib olish


def load_todos():
    if TODO_FILE.exists():
        with open(TODO_FILE, "r") as file:
            return json.load(file)
    return []

# Vazifalarni faylga saqlash


def save_todos(todos):
    with open(TODO_FILE, "w") as file:
        json.dump(todos, file)


@click.group()
def cli():
    """Todo List CLI Dasturi"""
    pass


@cli.command()
@click.argument('task')
def add(task):
    """Yangi vazifa qo'shish"""
    todos = load_todos()
    todos.append(task)
    save_todos(todos)
    click.echo(f"Vazifa qo‘shildi: {task}")


@cli.command()
def list():
    """Barcha vazifalarni ko‘rish"""
    todos = load_todos()
    if not todos:
        click.echo('Todo list bo‘sh.')
    else:
        click.echo('Todo List:')
        for i, task in enumerate(todos, 1):
            click.echo(f'{i}. {task}')


@cli.command()
@click.argument('index', type=int)
@click.argument('task')
def update(index, task):
    """Vazifani yangilash"""
    todos = load_todos()
    try:
        todos[index - 1] = task
        save_todos(todos)
        click.echo(f"Vazifa yangilandi: {task}")
    except IndexError:
        click.echo("Vazifa topilmadi!")


@cli.command()
@click.argument('index', type=int)
def remove(index):
    """Vazifani o‘chirish"""
    todos = load_todos()
    try:
        task = todos.pop(index - 1)
        save_todos(todos)
        click.echo(f"Vazifa o‘chirildi: {task}")
    except IndexError:
        click.echo("Vazifa topilmadi!")


if __name__ == '__main__':
    cli()
