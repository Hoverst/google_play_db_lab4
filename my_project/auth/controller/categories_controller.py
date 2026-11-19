from flask import request, jsonify, abort
from my_project.auth.dto import categories_dto
from my_project.auth.service import categories_service


def get_all():
    return jsonify(categories_service.get_all()), 200


def get_by_id(category_id):
    return jsonify(categories_service.get_by_id(category_id)), 200


def create():
    data = categories_dto.parse_create(request.get_json(silent=True))
    return jsonify(categories_service.create(data)), 201


def update(category_id):
    data = categories_dto.parse_put(request.get_json(silent=True))
    return jsonify(categories_service.update(category_id, data, partial=False)), 200


def patch(category_id):
    data = categories_dto.parse_patch(request.get_json(silent=True))
    return jsonify(categories_service.update(category_id, data, partial=True)), 200


def delete(category_id):
    categories_service.delete(category_id)
    return "", 204


def get_apps(category_id):
    from my_project.auth.service import apps_categories_service
    return jsonify(apps_categories_service.list_apps(category_id)), 200
