"""Routes for the accounts table and its relationship endpoints."""

from flask import Blueprint
from my_project.auth.controller import accounts_controller

accounts_bp = Blueprint('accounts', __name__, url_prefix='/accounts')

accounts_bp.add_url_rule('', view_func=accounts_controller.get_all, methods=['GET'])
accounts_bp.add_url_rule('/<int:account_id>', view_func=accounts_controller.get_by_id, methods=['GET'])
accounts_bp.add_url_rule('', view_func=accounts_controller.create, methods=['POST'])
accounts_bp.add_url_rule('/<int:account_id>', view_func=accounts_controller.update, methods=['PUT'])
accounts_bp.add_url_rule('/<int:account_id>', view_func=accounts_controller.delete, methods=['DELETE'])

# M:1 / M:M relationship endpoints
accounts_bp.add_url_rule('/<int:account_id>/companies', view_func=accounts_controller.get_companies, methods=['GET'])
accounts_bp.add_url_rule('/<int:account_id>/payment_cards', view_func=accounts_controller.get_payment_cards, methods=['GET'])
accounts_bp.add_url_rule('/<int:account_id>/reviews', view_func=accounts_controller.get_reviews, methods=['GET'])
accounts_bp.add_url_rule('/<int:account_id>/bills', view_func=accounts_controller.get_bills, methods=['GET'])
accounts_bp.add_url_rule('/<int:account_id>/library', view_func=accounts_controller.get_library, methods=['GET'])
accounts_bp.add_url_rule('/<int:account_id>/devices', view_func=accounts_controller.get_devices, methods=['GET'])
