"""Routes for the companies table and its relationship endpoints."""

from flask import Blueprint
from my_project.auth.controller import companies_controller

companies_bp = Blueprint('companies', __name__, url_prefix='/companies')

companies_bp.add_url_rule('', view_func=companies_controller.get_all, methods=['GET'])
companies_bp.add_url_rule('/<int:company_id>', view_func=companies_controller.get_by_id, methods=['GET'])
companies_bp.add_url_rule('', view_func=companies_controller.create, methods=['POST'])
companies_bp.add_url_rule('/<int:company_id>', view_func=companies_controller.update, methods=['PUT'])
companies_bp.add_url_rule('/<int:company_id>', view_func=companies_controller.delete, methods=['DELETE'])

# M:1 relationship endpoints
companies_bp.add_url_rule('/<int:company_id>/apps', view_func=companies_controller.get_apps, methods=['GET'])
