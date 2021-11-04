from flask import Blueprint, request
from src.models.category_model import category_model

category = Blueprint('category', __name__, url_prefix='/category')
category = category_model()

def get_category():
    return category.get_category()

@categorys.route('', methods=['POST'])
def create_category():
    data = request.form
    category.create_category(data)
    return 'category created succesfully!', 200
