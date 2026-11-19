from flask import request, jsonify, abort
from my_project.auth.dto import installations_dto
from my_project.auth.service import installations_service


def get_all():
    return jsonify(installations_service.get_all()), 200


def get_by_id(installation_id):
    return jsonify(installations_service.get_by_id(installation_id)), 200


def create():
    data = installations_dto.parse_create(request.get_json(silent=True))
    return jsonify(installations_service.create(data)), 201


def update(installation_id):
    data = installations_dto.parse_put(request.get_json(silent=True))
    return jsonify(installations_service.update(installation_id, data, partial=False)), 200


def patch(installation_id):
    data = installations_dto.parse_patch(request.get_json(silent=True))
    return jsonify(installations_service.update(installation_id, data, partial=True)), 200


def delete(installation_id):
    installations_service.delete(installation_id)
    return "", 204
