from flask import Blueprint, request
from src.models.project_model import project_model

project_route = Blueprint('project', __name__, url_prefix='/'project)
project = project_model()

def get_project():
    return project.get_project()

@project_route.route('', methods=['POST'])
def create_project():
    data = request.form
    project.create_project(data)
    return 'project created successfully!', 200
