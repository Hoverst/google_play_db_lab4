from flask import Blueprint
from my_project.auth.controller import apps_categories_controller

apps_categories_bp = Blueprint('apps_categories', __name__, url_prefix='/apps_categories')

apps_categories_bp.add_url_rule('', view_func=apps_categories_controller.get_all, methods=['GET'])
apps_categories_bp.add_url_rule(
    '/<int:app_id>/<int:category_id>',
    view_func=apps_categories_controller.get_by_id,
    methods=['GET']
)
apps_categories_bp.add_url_rule('', view_func=apps_categories_controller.create, methods=['POST'])
apps_categories_bp.add_url_rule(
    '/<int:app_id>/<int:category_id>',
    view_func=apps_categories_controller.update,
    methods=['PUT']
)
apps_categories_bp.add_url_rule(
    '/<int:app_id>/<int:category_id>',
    view_func=apps_categories_controller.patch,
    methods=['PATCH']
)
apps_categories_bp.add_url_rule(
    '/<int:app_id>/<int:category_id>',
    view_func=apps_categories_controller.delete,
    methods=['DELETE']
)
