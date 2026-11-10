from flask import Blueprint
from my_project.auth.controller import apps_controller

apps_bp = Blueprint('apps', __name__, url_prefix='/apps')

apps_bp.add_url_rule('', view_func=apps_controller.get_all, methods=['GET'])
apps_bp.add_url_rule('/<int:app_id>', view_func=apps_controller.get_by_id, methods=['GET'])
apps_bp.add_url_rule('', view_func=apps_controller.create, methods=['POST'])
apps_bp.add_url_rule('/<int:app_id>', view_func=apps_controller.update, methods=['PUT'])
apps_bp.add_url_rule('/<int:app_id>', view_func=apps_controller.patch, methods=['PATCH'])
apps_bp.add_url_rule('/<int:app_id>', view_func=apps_controller.delete, methods=['DELETE'])

apps_bp.add_url_rule('/<int:app_id>/versions', view_func=apps_controller.get_versions, methods=['GET'])
apps_bp.add_url_rule('/<int:app_id>/discounts', view_func=apps_controller.get_discounts, methods=['GET'])
apps_bp.add_url_rule('/<int:app_id>/reviews', view_func=apps_controller.get_reviews, methods=['GET'])
apps_bp.add_url_rule('/<int:app_id>/bills', view_func=apps_controller.get_bills, methods=['GET'])
apps_bp.add_url_rule('/<int:app_id>/library', view_func=apps_controller.get_library, methods=['GET'])
apps_bp.add_url_rule('/<int:app_id>/installations', view_func=apps_controller.get_installations, methods=['GET'])
apps_bp.add_url_rule('/<int:app_id>/categories', view_func=apps_controller.get_categories, methods=['GET'])
