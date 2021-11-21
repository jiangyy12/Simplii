from flask import Blueprint, request
from src.models.project_model import project_model

# project = Blueprint('project', __name__, url_prefix='/project')
# project = project_model()

# def get_project():
#     return project.get_project()
    
# @project_route('', methods=['POST'])
# def create_project():
#     data = request.form
#     project.create_project(data)
#     return redirect('/view_all_projects')

projects = Blueprint('projects', __name__, url_prefix='/projects')

project = project_model()

def get_project():
    return project.get_project()

@projects.route('', methods=['POST'])
def create_project():
    data = request.form
    project.create_project(data)
    return redirect('/view_all_projects')

@tasks.route('', methods=['DELETE'])
def delete_task():
    taskid = request.form['taskid']
    task.delete_task(taskid)
    return 'Task Deleted', 200

@tasks.route('/update', methods=['POST'])
def update_task():
    data = request.form
    task.update_task(data)
    return 'Task updated succesfully!', 200
