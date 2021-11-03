from flask import Blueprint
from controller import (task_controller)


routes = Blueprint('routes', __name__)

routes.register_blueprint(task_controller.task, url_prefix='/tasks')