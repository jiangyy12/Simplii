from flask import Blueprint, request
from src.models.task_model import task_model

tasks = Blueprint('tasks', __name__, url_prefix='/tasks')
task = task_model()


@tasks.route('', methods=['GET'])
def get_tasks():
    if 'THIS WEEK' in request.json:
        return task.get_this_week_tasks()
    if 'BACKLOG' in request.json:
        return task.get_backlog()
    if 'FUTURE TASKS' in request.json:
        return task.get_future_tasks()


@tasks.route('', methods=['POST'])
def create_task():
    data = request.form
    return task.create_tasks(data)
