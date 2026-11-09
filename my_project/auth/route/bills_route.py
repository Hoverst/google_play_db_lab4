"""Routes for the bills table (composite PK)."""

from flask import Blueprint
from my_project.auth.controller import bills_controller

bills_bp = Blueprint('bills', __name__, url_prefix='/bills')

bills_bp.add_url_rule('', view_func=bills_controller.get_all, methods=['GET'])
bills_bp.add_url_rule(
    '/<int:account_id>/<int:app_id>',
    view_func=bills_controller.get_by_id,
    methods=['GET']
)
bills_bp.add_url_rule('', view_func=bills_controller.create, methods=['POST'])
bills_bp.add_url_rule(
    '/<int:account_id>/<int:app_id>',
    view_func=bills_controller.update,
    methods=['PUT']
)
bills_bp.add_url_rule(
    '/<int:account_id>/<int:app_id>',
    view_func=bills_controller.delete,
    methods=['DELETE']
)
