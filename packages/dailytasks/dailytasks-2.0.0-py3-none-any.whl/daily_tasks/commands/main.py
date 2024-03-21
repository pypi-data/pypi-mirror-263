import click as ck
from daily_tasks.commands.main_commands import add, view
from daily_tasks.commands.modification_commands import modify
from daily_tasks.commands.removal_commands import delete
from daily_tasks.commands.filter_commands import filter_tasks


@ck.group
def daily_tasks() -> None:
    """A tasks manager for those who like work from shell."""


daily_tasks.add_command(add)
daily_tasks.add_command(view)
daily_tasks.add_command(modify)
daily_tasks.add_command(delete)
daily_tasks.add_command(filter_tasks, name='filter')
