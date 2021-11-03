from flask import Blueprint
from src.controller import (task_controller)


routes = Blueprint('routes', __name__)

routes.register_blueprint(task_controller.tasks, url_prefix='/tasks')