"""Routes for the reviews table (composite PK)."""

from flask import Blueprint
from my_project.auth.controller import reviews_controller

reviews_bp = Blueprint('reviews', __name__, url_prefix='/reviews')

reviews_bp.add_url_rule('', view_func=reviews_controller.get_all, methods=['GET'])
reviews_bp.add_url_rule(
    '/<int:account_id>/<int:app_id>',
    view_func=reviews_controller.get_by_id,
    methods=['GET']
)
reviews_bp.add_url_rule('', view_func=reviews_controller.create, methods=['POST'])
reviews_bp.add_url_rule(
    '/<int:account_id>/<int:app_id>',
    view_func=reviews_controller.update,
    methods=['PUT']
)
reviews_bp.add_url_rule(
    '/<int:account_id>/<int:app_id>',
    view_func=reviews_controller.delete,
    methods=['DELETE']
)
