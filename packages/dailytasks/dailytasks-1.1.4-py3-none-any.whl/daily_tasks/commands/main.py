import click as ck
from daily_tasks.commands.main_commands import add_task, view_tasks
from daily_tasks.commands.modification_commands import modify_description, modify_priority, modify_due_date, modify_status
from daily_tasks.commands.removal_commands import delete_done_tasks, delete_task
from daily_tasks.commands.filter_commands import filter_tasks_by_priority, filter_tasks_by_due_date, filter_tasks_by_status


@ck.group
def daily_tasks() -> None:
    """A tasks manager for those who like work from shell."""


daily_tasks.add_command(add_task)
daily_tasks.add_command(view_tasks)
daily_tasks.add_command(modify_description)
daily_tasks.add_command(modify_priority)
daily_tasks.add_command(modify_due_date)
daily_tasks.add_command(modify_status)
daily_tasks.add_command(delete_done_tasks)
daily_tasks.add_command(delete_task)
daily_tasks.add_command(filter_tasks_by_priority)
daily_tasks.add_command(filter_tasks_by_due_date)
daily_tasks.add_command(filter_tasks_by_status)
