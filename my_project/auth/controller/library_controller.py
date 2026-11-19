from flask import request, jsonify, abort
from my_project.auth.dto import library_dto
from my_project.auth.service import library_service


def get_all():
    return jsonify(library_service.get_all()), 200


def get_by_id(entry_id):
    return jsonify(library_service.get_by_id(entry_id)), 200


def create():
    data = library_dto.parse_create(request.get_json(silent=True))
    return jsonify(library_service.create(data)), 201


def update(entry_id):
    data = library_dto.parse_put(request.get_json(silent=True))
    return jsonify(library_service.update(entry_id, data, partial=False)), 200


def patch(entry_id):
    data = library_dto.parse_patch(request.get_json(silent=True))
    return jsonify(library_service.update(entry_id, data, partial=True)), 200


def delete(entry_id):
    library_service.delete(entry_id)
    return "", 204
