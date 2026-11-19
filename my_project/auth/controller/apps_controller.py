from flask import request, jsonify, abort
from my_project.auth.dto import apps_dto
from my_project.auth.service import apps_service


def get_all():
    return jsonify(apps_service.get_all()), 200


def get_by_id(app_id):
    return jsonify(apps_service.get_by_id(app_id)), 200


def create():
    data = apps_dto.parse_create(request.get_json(silent=True))
    return jsonify(apps_service.create(data)), 201


def update(app_id):
    data = apps_dto.parse_put(request.get_json(silent=True))
    return jsonify(apps_service.update(app_id, data, partial=False)), 200


def patch(app_id):
    data = apps_dto.parse_patch(request.get_json(silent=True))
    return jsonify(apps_service.update(app_id, data, partial=True)), 200


def delete(app_id):
    result = apps_service.delete(app_id)
    if result is None:
        return "", 204
    return jsonify(result), 200


def get_categories(app_id):
    from my_project.auth.service import apps_categories_service
    return jsonify(apps_categories_service.list_categories(app_id)), 200


def attach_category(app_id):
    from my_project.auth.service import apps_categories_service
    from my_project.auth.dto._common import require_dict, as_pos_int
    data = require_dict(request.get_json(silent=True))
    category_id = as_pos_int(data, "category_id")
    return jsonify(apps_categories_service.attach(app_id, category_id)), 201


def detach_category(app_id, category_id):
    from my_project.auth.service import apps_categories_service
    apps_categories_service.detach(app_id, category_id)
    return "", 204


def get_versions(app_id):
    from my_project.auth.dao import apps_dao
    app = apps_dao.find_by_id(app_id)
    if app is None:
        abort(404)
    return jsonify([v.to_dict() for v in app.versions]), 200


def get_reviews(app_id):
    from my_project.auth.dao import apps_dao
    app = apps_dao.find_by_id(app_id)
    if app is None:
        abort(404)
    return jsonify([r.to_dict() for r in app.reviews]), 200


def get_library(app_id):
    from my_project.auth.dao import apps_dao
    app = apps_dao.find_by_id(app_id)
    if app is None:
        abort(404)
    return jsonify([e.to_dict() for e in app.library_entries]), 200
