from daily_tasks.commands import utilities
from datetime import datetime # pylint: disable=unused-import
import json
import click as ck


@ck.command
@ck.option('-id', '--task-id',
           required=True,
           type=ck.INT
           )
@ck.option('-d', '--new-description',
           required=True,
           type=ck.STRING
           )
def modify_description(task_id, new_description) -> None:
    """Modify description of a task."""
    with open(utilities.tasks_file_path, 'r', encoding='utf-8') as tasks_file_read:
        tasks = json.load(tasks_file_read)

    for task in tasks:
        if task['id'] == task_id:
            extracted_task = task
            break

    task_index = tasks.index(extracted_task)

    extracted_task['description'] = new_description.capitalize()

    tasks.pop(task_index)
    tasks.insert(task_index, extracted_task)

    with open(utilities.tasks_file_path, 'w', encoding='utf-8') as tasks_file_write:
        json.dump(tasks, tasks_file_write, indent=2)


@ck.command
@ck.option('-id', '--task-id',
           required=True,
           type=ck.INT
           )
@ck.option('-p', '--new-priority',
           required=True,
           type=ck.Choice(utilities.PRIORITIES, case_sensitive=False)
           )
def modify_priority(task_id, new_priority):
    """Modify priority of a task."""
    with open(utilities.tasks_file_path, 'r', encoding='utf-8') as tasks_file_read:
        tasks = json.load(tasks_file_read)

    for task in tasks:
        if task['id'] == task_id:
            extracted_task = task
            break

    task_index = tasks.index(extracted_task)

    new_priority_upper = new_priority.upper()
    extracted_task['priority'] = new_priority_upper

    tasks.pop(task_index)
    tasks.insert(task_index, extracted_task)

    with open(utilities.tasks_file_path, 'w', encoding='utf-8') as tasks_file_write:
        json.dump(tasks, tasks_file_write, indent=2)


@ck.command
@ck.option('-id', '--task-id',
           required=True,
           type=ck.INT
           )
@ck.option('-dd', '--new-due-date',
           required=True,
           type=ck.DateTime(formats=utilities.DUE_DATE_FORMAT)
           )
def modify_due_date(task_id, new_due_date):
    """Modify due date of a task."""
    with open(utilities.tasks_file_path, 'r', encoding='utf-8') as tasks_file_read:
        tasks = json.load(tasks_file_read)

    for task in tasks:
        if task['id'] == task_id:
            extracted_task = task
            break

    task_index = tasks.index(extracted_task)

    new_due_date_date_object = new_due_date.date()
    new_due_date_formatted = new_due_date_date_object.strftime(utilities.DUE_DATE_FORMAT[0])

    extracted_task['due_date'] = new_due_date_formatted

    tasks.pop(task_index)
    tasks.insert(task_index, extracted_task)

    with open(utilities.tasks_file_path, 'w', encoding='utf-8') as tasks_file_write:
        json.dump(tasks, tasks_file_write, indent=2)


@ck.command
@ck.option('-id', '--task-id',
           required=True,
           type=ck.INT
           )
@ck.option('-s', '--new-status',
           required=True,
           type=ck.Choice(choices=utilities.STATUS, case_sensitive=False)
           )
def modify_status(task_id, new_status):
    """Modify status of a task."""
    with open(utilities.tasks_file_path, 'r', encoding='utf-8') as tasks_file_read:
        tasks = json.load(tasks_file_read)

    for task in tasks:
        if task['id'] == task_id:
            extracted_task = task
            break

    task_index = tasks.index(extracted_task)

    new_status_capitalize = new_status.capitalize()
    extracted_task['status'] = new_status_capitalize

    tasks.pop(task_index)
    tasks.insert(task_index, extracted_task)

    with open(utilities.tasks_file_path, 'w', encoding='utf-8') as tasks_file_write:
        json.dump(tasks, tasks_file_write, indent=2)
