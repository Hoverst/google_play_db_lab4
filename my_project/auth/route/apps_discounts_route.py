from flask import Blueprint
from my_project.auth.controller import apps_discounts_controller

apps_discounts_bp = Blueprint('apps_discounts', __name__, url_prefix='/apps_discounts')

apps_discounts_bp.add_url_rule('', view_func=apps_discounts_controller.get_all, methods=['GET'])
apps_discounts_bp.add_url_rule('/<int:discount_id>', view_func=apps_discounts_controller.get_by_id, methods=['GET'])
apps_discounts_bp.add_url_rule('', view_func=apps_discounts_controller.create, methods=['POST'])
apps_discounts_bp.add_url_rule('/<int:discount_id>', view_func=apps_discounts_controller.update, methods=['PUT'])
apps_discounts_bp.add_url_rule('/<int:discount_id>', view_func=apps_discounts_controller.patch, methods=['PATCH'])
apps_discounts_bp.add_url_rule('/<int:discount_id>', view_func=apps_discounts_controller.delete, methods=['DELETE'])

apps_discounts_bp.add_url_rule(
    '/<int:discount_id>/bills',
    view_func=apps_discounts_controller.get_bills,
    methods=['GET']
)
