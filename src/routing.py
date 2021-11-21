from flask import Blueprint
from src.controller import (task_controller)
from src.controller import (project_controller)
from src.controller import (category_controller)
routes = Blueprint('routes', __name__)

routes.register_blueprint(task_controller.tasks, url_prefix='/tasks')
routes.register_blueprint(project_controller.projects, url_prefix='/projects')
routes.register_blueprint(category_controller.category, url_prefix='/category')