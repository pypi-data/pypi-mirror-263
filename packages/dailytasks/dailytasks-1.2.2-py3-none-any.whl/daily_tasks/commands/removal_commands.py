import json
import click as ck
from daily_tasks.commands import utilities


@ck.command
def delete_done_tasks():
    """Delete all your done tasks."""
    with open(utilities.tasks_file_path, 'r', encoding='utf-8') as reading_tasks_file:
        tasks = json.load(reading_tasks_file)

    done_status = utilities.STATUS[2]

    for task in tasks:
        if task['status'] == done_status:
            task_index = tasks.index(task)
            tasks.pop(task_index)
    
    with open(utilities.tasks_file_path, 'w', encoding='utf-8') as writing_tasks_file:
        json.dump(tasks, writing_tasks_file, indent=2)


@ck.command
@ck.option('-id', '--task-id',
           required=True,
           type=ck.INT)
def delete_task(task_id):
    """Delete a task."""
    with open(utilities.tasks_file_path, 'r', encoding='utf-8') as reading_tasks_file:
        tasks = json.load(reading_tasks_file)

    for task in tasks:
        if task['id'] == task_id:
            task_index = tasks.index(task)
            tasks.pop(task_index)
            ck.echo(ck.style('Task deleted successfully.',
                             bold=True))

    with open(utilities.tasks_file_path, 'w', encoding='utf-8') as writing_tasks_file:
        json.dump(tasks, writing_tasks_file, indent=2)

