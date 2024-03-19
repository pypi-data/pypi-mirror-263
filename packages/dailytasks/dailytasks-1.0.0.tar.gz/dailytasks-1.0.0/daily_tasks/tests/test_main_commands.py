from click.testing import CliRunner

from daily_tasks.commands.main_commands import view_tasks, add_task, create_tasks_file


def test_create_tasks_file():
    runner = CliRunner()
    test_task_data_file = 'Tasks_test.json'
    result = runner.invoke(create_tasks_file, ['--file_name', test_task_data_file])
    assert result.exit_code == 0, f"Command failed: {result.exception}\n{result.output}"

def test_add_task():
    runner = CliRunner()

    description = "Complete unit test"
    priority = "H"
    due_date = "2024/03/15"
    status = "To-do"
    test_task_data_file = "Tasks_test.json"

    result = runner.invoke(add_task, [
        '--description', description,
        '--priority', priority,
        '--due-date', due_date,
        '--status', status,
        '--file_name', test_task_data_file,
    ])

    assert result.exit_code == 0, f"Command failed: {result.exception}\n{result.output}"

def test_view_tasks():
    runner = CliRunner()
    test_task_data_file = 'Tasks_test.json'
    result = runner.invoke(view_tasks, ['--file_name', test_task_data_file])

    assert result.exit_code == 0, f"Command failed: {result.exception}\n{result.output}"

test_create_tasks_file()
test_add_task()
test_view_tasks()
