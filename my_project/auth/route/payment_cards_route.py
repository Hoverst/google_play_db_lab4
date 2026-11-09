"""Routes for the payment_cards table and its relationship endpoints."""

from flask import Blueprint
from my_project.auth.controller import payment_cards_controller

payment_cards_bp = Blueprint('payment_cards', __name__, url_prefix='/payment_cards')

payment_cards_bp.add_url_rule('', view_func=payment_cards_controller.get_all, methods=['GET'])
payment_cards_bp.add_url_rule('/<int:card_id>', view_func=payment_cards_controller.get_by_id, methods=['GET'])
payment_cards_bp.add_url_rule('', view_func=payment_cards_controller.create, methods=['POST'])
payment_cards_bp.add_url_rule('/<int:card_id>', view_func=payment_cards_controller.update, methods=['PUT'])
payment_cards_bp.add_url_rule('/<int:card_id>', view_func=payment_cards_controller.delete, methods=['DELETE'])

# M:1 relationship endpoints
payment_cards_bp.add_url_rule(
    '/<int:card_id>/bills',
    view_func=payment_cards_controller.get_bills,
    methods=['GET']
)
