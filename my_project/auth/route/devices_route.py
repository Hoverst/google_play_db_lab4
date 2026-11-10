from flask import Blueprint
from my_project.auth.controller import devices_controller

devices_bp = Blueprint('devices', __name__, url_prefix='/devices')

devices_bp.add_url_rule('', view_func=devices_controller.get_all, methods=['GET'])
devices_bp.add_url_rule('/<int:device_id>', view_func=devices_controller.get_by_id, methods=['GET'])
devices_bp.add_url_rule('', view_func=devices_controller.create, methods=['POST'])
devices_bp.add_url_rule('/<int:device_id>', view_func=devices_controller.update, methods=['PUT'])
devices_bp.add_url_rule('/<int:device_id>', view_func=devices_controller.patch, methods=['PATCH'])
devices_bp.add_url_rule('/<int:device_id>', view_func=devices_controller.delete, methods=['DELETE'])

devices_bp.add_url_rule('/<int:device_id>/installations', view_func=devices_controller.get_installations, methods=['GET'])
devices_bp.add_url_rule('/<int:device_id>/accounts', view_func=devices_controller.get_accounts, methods=['GET'])
