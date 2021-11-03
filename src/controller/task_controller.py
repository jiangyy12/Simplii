from flask import Blueprint, request
from src.models.task_model import task_model

tasks = Blueprint('tasks', __name__, url_prefix='/tasks')
task = task_model()


@tasks.route('', methods=['GET'])
def get_tasks():
    if 'period' not in request.json:
        return 'Need time period to fetch tasks!'

    if request.json['period'] == 'THIS WEEK':
        return task.get_this_week_tasks()
    if request.json['period'] == 'BACKLOG':
        return task.get_backlog()
    if request.json['period'] == 'FUTURE TASKS':
        return task.get_future_tasks()

@tasks.route('', methods=['POST'])
def create_task():
    data = request.form
    return task.create_tasks(data)
