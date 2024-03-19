"""Utilities"""
from datetime import datetime
from os import listdir
import click as ck


DUE_DATE_FORMAT = ['%Y/%m/%d']
PRIORITIES = ['H', 'M', 'L', ' ']
STATUS = ['To-do', 'In-progress', 'Done', ' ']

def get_due_date_default_value() -> str:
    """Get default value for due_date parameter"""
    today_datetime_obj = datetime.today()
    today_date_obj = today_datetime_obj.date()
    today_date_obj_formatted = today_date_obj.strftime(DUE_DATE_FORMAT[0])
    today_date_str_formatted = str(today_date_obj_formatted)

    return today_date_str_formatted

def check_if_a_json_file_exist() -> str:
    files = listdir('.')

    for file in files:
        if file.endswith('.json'):
            tasks_file = file
            break
        tasks_file = None
        continue

    return tasks_file

def stylized_tasks_printing(task_id, description, priority, due_date, status) -> None:
    if priority == PRIORITIES[0]:
        if status == STATUS[0]:
            ck.echo('{}. {} - {} - {} - {}'.format(
                ck.style(text=task_id, fg='black'),
                description,
                ck.style(text=priority, fg='red', bold=True),
                ck.style(text=status, fg='red'),
                ck.style(text=due_date, bold=True)
            ))
        elif status == STATUS[1]:
            ck.echo('{}. {} - {} - {} - {}'.format(
                ck.style(text=task_id, fg='black'),
                description,
                ck.style(text=priority, fg='red', bold=True),
                ck.style(text=status, fg='yellow'),
                ck.style(text=due_date, bold=True)
            ))
        else:
            ck.echo('{}. {} - {} - {} - {}'.format(
                ck.style(text=task_id, fg='black'),
                description,
                ck.style(text=priority, fg='red', bold=True),
                ck.style(text=status, fg='green'),
                ck.style(text=due_date, bold=True)
            ))
    elif priority == PRIORITIES[1]:
        if status == STATUS[0]:
            ck.echo('{}. {} - {} - {} - {}'.format(
                ck.style(text=task_id, fg='black'),
                description,
                ck.style(text=priority, fg='yellow', bold=True),
                ck.style(text=status, fg='red'),
                ck.style(text=due_date, bold=True)
            ))
        elif status == STATUS[1]:
            ck.echo('{}. {} - {} - {} - {}'.format(
                ck.style(text=task_id, fg='black'),
                description,
                ck.style(text=priority, fg='yellow', bold=True),
                ck.style(text=status, fg='yellow'),
                ck.style(text=due_date, bold=True)
            ))
        else:
            ck.echo('{}. {} - {} - {} - {}'.format(
                ck.style(text=task_id, fg='black'),
                description,
                ck.style(text=priority, fg='yellow', bold=True),
                ck.style(text=status, fg='green'),
                ck.style(text=due_date, bold=True)
            ))
    else:
        if status == STATUS[0]:
            ck.echo('{}. {} - {} - {} - {}'.format(
                ck.style(text=task_id, fg='black'),
                description,
                ck.style(text=priority, fg='white', bold=True),
                ck.style(text=status, fg='red'),
                ck.style(text=due_date, bold=True)
            ))
        elif status == STATUS[1]:
            ck.echo('{}. {} - {} - {} - {}'.format(
                ck.style(text=task_id, fg='black'),
                description,
                ck.style(text=priority, fg='white', bold=True),
                ck.style(text=status, fg='yellow'),
                ck.style(text=due_date, bold=True)
            ))
        else:
            ck.echo('{}. {} - {} - {} - {}'.format(
                ck.style(text=task_id, fg='black'),
                description,
                ck.style(text=priority, fg='white', bold=True),
                ck.style(text=status, fg='green'),
                ck.style(text=due_date, bold=True)
            ))
