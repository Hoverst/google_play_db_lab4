"""Routes for the library table (composite PK)."""

from flask import Blueprint
from my_project.auth.controller import library_controller

library_bp = Blueprint('library', __name__, url_prefix='/library')

library_bp.add_url_rule('', view_func=library_controller.get_all, methods=['GET'])
library_bp.add_url_rule(
    '/<int:app_id>/<int:account_id>',
    view_func=library_controller.get_by_id,
    methods=['GET']
)
library_bp.add_url_rule('', view_func=library_controller.create, methods=['POST'])
library_bp.add_url_rule(
    '/<int:app_id>/<int:account_id>',
    view_func=library_controller.update,
    methods=['PUT']
)
library_bp.add_url_rule(
    '/<int:app_id>/<int:account_id>',
    view_func=library_controller.delete,
    methods=['DELETE']
)
