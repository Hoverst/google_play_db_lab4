"""Routes for the installations table (composite PK)."""

from flask import Blueprint
from my_project.auth.controller import installations_controller

installations_bp = Blueprint('installations', __name__, url_prefix='/installations')

installations_bp.add_url_rule('', view_func=installations_controller.get_all, methods=['GET'])
installations_bp.add_url_rule(
    '/<int:app_id>/<int:device_id>',
    view_func=installations_controller.get_by_id,
    methods=['GET']
)
installations_bp.add_url_rule('', view_func=installations_controller.create, methods=['POST'])
installations_bp.add_url_rule(
    '/<int:app_id>/<int:device_id>',
    view_func=installations_controller.update,
    methods=['PUT']
)
installations_bp.add_url_rule(
    '/<int:app_id>/<int:device_id>',
    view_func=installations_controller.delete,
    methods=['DELETE']
)
