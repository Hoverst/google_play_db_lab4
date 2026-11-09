"""Routes for the categories table and its relationship endpoints."""

from flask import Blueprint
from my_project.auth.controller import categories_controller

categories_bp = Blueprint('categories', __name__, url_prefix='/categories')

categories_bp.add_url_rule('', view_func=categories_controller.get_all, methods=['GET'])
categories_bp.add_url_rule('/<int:category_id>', view_func=categories_controller.get_by_id, methods=['GET'])
categories_bp.add_url_rule('', view_func=categories_controller.create, methods=['POST'])
categories_bp.add_url_rule('/<int:category_id>', view_func=categories_controller.update, methods=['PUT'])
categories_bp.add_url_rule('/<int:category_id>', view_func=categories_controller.delete, methods=['DELETE'])

# M:M relationship endpoints
categories_bp.add_url_rule('/<int:category_id>/apps', view_func=categories_controller.get_apps, methods=['GET'])
