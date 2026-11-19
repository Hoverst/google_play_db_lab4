from flask import request, jsonify, abort
from my_project.auth.dto import apps_versions_dto
from my_project.auth.service import apps_versions_service


def get_all():
    return jsonify(apps_versions_service.get_all()), 200


def get_by_id(version_id):
    return jsonify(apps_versions_service.get_by_id(version_id)), 200


def create():
    data = apps_versions_dto.parse_create(request.get_json(silent=True))
    return jsonify(apps_versions_service.create(data)), 201


def update(version_id):
    data = apps_versions_dto.parse_put(request.get_json(silent=True))
    return jsonify(apps_versions_service.update(version_id, data, partial=False)), 200


def patch(version_id):
    data = apps_versions_dto.parse_patch(request.get_json(silent=True))
    return jsonify(apps_versions_service.update(version_id, data, partial=True)), 200


def delete(version_id):
    apps_versions_service.delete(version_id)
    return "", 204


def get_installations(version_id):
    from my_project.auth.dao import apps_versions_dao
    version = apps_versions_dao.find_by_id(version_id)
    if version is None:
        abort(404)
    return jsonify([i.to_dict() for i in version.installations]), 200
