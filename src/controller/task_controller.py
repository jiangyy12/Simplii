from flask import Blueprint, request
from src.models.task_model import task_model

tasks = Blueprint('tasks', __name__, url_prefix='/tasks')
task = task_model()

def get_tasks():
    if 'period' not in request.form:
        return 'Need time period to fetch tasks!'
    if request.form['period'] == 'THIS WEEK':
        return task.get_this_week_tasks()
    if request.form['period'] == 'BACKLOG':
        return task.get_backlog()
    if request.form['period'] == 'FUTURE TASKS':
        return task.get_future_tasks()

@tasks.route('', methods=['POST'])
def create_task():
    data = request.form
    task.create_tasks(data)
    return 'Task created succesfully!', 200

@tasks.route('', methods=['DELETE'])
def delete_task():
    taskid = request.form['taskid']
    task.delete_task(taskid)
    return 'Task Deleted', 200

@tasks.route('', methods=['POST'])
def update_task():
    data = request.form
    task.update_task(data)
    return 'Task updated succesfully!', 200


