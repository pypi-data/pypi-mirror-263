from datetime import datetime # pylint: disable=unused-import
import json
import click as ck
from daily_tasks.commands import utilities


@ck.command
@ck.option('-p', '--priority',
           required=True,
           type=ck.Choice(utilities.PRIORITIES, case_sensitive=False)
           )
def filter_tasks_by_priority(priority):
    """Filter your tasks by priority."""
    with open(utilities.tasks_file_path, 'r', encoding='utf-8') as reading_tasks_file:
        tasks = json.load(reading_tasks_file)

    priority_upper = priority.upper()

    for task in tasks:
        if task['priority'] == priority_upper:

            task_id = task['id']
            description = task['description']
            priority = task['priority']
            due_date = task['due_date']
            status = task['status']

            utilities.stylized_tasks_printing(task_id, description, priority, due_date, status)


@ck.command
@ck.option('-dd', '--due-date',
           required=True,
           type=ck.DateTime(formats=utilities.DUE_DATE_FORMAT)
           )
def filter_tasks_by_due_date(due_date):
    """Filter your tasks by due date."""
    with open(utilities.tasks_file_path, 'r', encoding='utf-8') as reading_tasks_file:
        tasks = json.load(reading_tasks_file)

    due_date_date_object = due_date.date()
    due_date_formatted = due_date_date_object.strftime(utilities.DUE_DATE_FORMAT[0])

    for task in tasks:
        if task['due_date'] == due_date_formatted:

            task_id = task['id']
            description = task['description']
            priority = task['priority']
            due_date = task['due_date']
            status = task['status']

            utilities.stylized_tasks_printing(task_id, description, priority, due_date, status)


@ck.command
@ck.option('-s', '--status',
           required=True,
           type=ck.Choice(utilities.STATUS, case_sensitive=False))
def filter_tasks_by_status(status):
    """Filter your tasks by status."""
    with open(utilities.tasks_file_path, 'r', encoding='utf-8') as reading_tasks_file:
        tasks = json.load(reading_tasks_file)

    status_capitalize = status.capitalize()

    for task in tasks:
        if task['status'] == status_capitalize:

            task_id = task['id']
            description = task['description']
            priority = task['priority']
            due_date = task['due_date']
            status = task['status']

            utilities.stylized_tasks_printing(task_id, description, priority, due_date, status)
