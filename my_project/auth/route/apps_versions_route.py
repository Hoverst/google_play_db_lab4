"""Routes for the apps_versions table."""

from flask import Blueprint
from my_project.auth.controller import apps_versions_controller

apps_versions_bp = Blueprint('apps_versions', __name__, url_prefix='/apps_versions')

apps_versions_bp.add_url_rule('', view_func=apps_versions_controller.get_all, methods=['GET'])
apps_versions_bp.add_url_rule('/<int:version_id>', view_func=apps_versions_controller.get_by_id, methods=['GET'])
apps_versions_bp.add_url_rule('', view_func=apps_versions_controller.create, methods=['POST'])
apps_versions_bp.add_url_rule('/<int:version_id>', view_func=apps_versions_controller.update, methods=['PUT'])
apps_versions_bp.add_url_rule('/<int:version_id>', view_func=apps_versions_controller.delete, methods=['DELETE'])
