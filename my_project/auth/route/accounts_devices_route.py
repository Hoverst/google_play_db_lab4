from flask import Blueprint
from my_project.auth.controller import accounts_devices_controller

accounts_devices_bp = Blueprint('accounts_devices', __name__, url_prefix='/accounts_devices')

accounts_devices_bp.add_url_rule('', view_func=accounts_devices_controller.get_all, methods=['GET'])
accounts_devices_bp.add_url_rule(
    '/<int:account_id>/<int:device_id>',
    view_func=accounts_devices_controller.get_by_id,
    methods=['GET']
)
accounts_devices_bp.add_url_rule('', view_func=accounts_devices_controller.create, methods=['POST'])
accounts_devices_bp.add_url_rule(
    '/<int:account_id>/<int:device_id>',
    view_func=accounts_devices_controller.update,
    methods=['PUT']
)
accounts_devices_bp.add_url_rule(
    '/<int:account_id>/<int:device_id>',
    view_func=accounts_devices_controller.patch,
    methods=['PATCH']
)
accounts_devices_bp.add_url_rule(
    '/<int:account_id>/<int:device_id>',
    view_func=accounts_devices_controller.delete,
    methods=['DELETE']
)
