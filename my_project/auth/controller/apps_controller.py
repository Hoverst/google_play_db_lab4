from flask import request, jsonify, abort
from sqlalchemy.exc import IntegrityError
from my_project import db
from my_project.auth.domain.apps import App
from my_project.auth.service import apps_service

def get_all():
    result = apps_service.get_all()
    return jsonify(result), 200

def get_by_id(app_id):
    result = apps_service.get_by_id(app_id)
    return jsonify(result), 200

def create():
    data = request.get_json(silent=True)
    if data is None:
        return jsonify({"error": "No input data provided"}), 400
    try:
        result = apps_service.create(data)
        return jsonify(result), 201
    except IntegrityError as e:
        db.session.rollback()
        return jsonify({"error": "Integrity constraint violated: " + str(e.orig)}), 409

def update(app_id):
    data = request.get_json(silent=True)
    if data is None:
        return jsonify({"error": "No input data provided"}), 400
    try:
        result = apps_service.update(app_id, data, partial=False)
        return jsonify(result), 200
    except IntegrityError as e:
        db.session.rollback()
        return jsonify({"error": "Integrity constraint violated: " + str(e.orig)}), 409

def patch(app_id):
    data = request.get_json(silent=True)
    if data is None:
        return jsonify({"error": "No input data provided"}), 400
    try:
        result = apps_service.update(app_id, data, partial=True)
        return jsonify(result), 200
    except IntegrityError as e:
        db.session.rollback()
        return jsonify({"error": "Integrity constraint violated: " + str(e.orig)}), 409

def delete(app_id):
    try:
        apps_service.delete(app_id)
        return "", 204
    except IntegrityError as e:
        db.session.rollback()
        return jsonify({"error": "Integrity constraint violated: " + str(e.orig)}), 409

def get_versions(app_id):
    app = App.query.get(app_id)
    if app is None:
        abort(404)
    return jsonify([item.to_dict() for item in app.versions]), 200

def get_discounts(app_id):
    app = App.query.get(app_id)
    if app is None:
        abort(404)
    return jsonify([item.to_dict() for item in app.discounts]), 200

def get_reviews(app_id):
    app = App.query.get(app_id)
    if app is None:
        abort(404)
    return jsonify([item.to_dict() for item in app.reviews]), 200

def get_bills(app_id):
    app = App.query.get(app_id)
    if app is None:
        abort(404)
    return jsonify([item.to_dict() for item in app.bills]), 200

def get_library(app_id):
    app = App.query.get(app_id)
    if app is None:
        abort(404)
    return jsonify([item.to_dict() for item in app.library_entries]), 200

def get_installations(app_id):
    app = App.query.get(app_id)
    if app is None:
        abort(404)
    return jsonify([item.to_dict() for item in app.installations]), 200

def get_categories(app_id):
    app = App.query.get(app_id)
    if app is None:
        abort(404)
    return jsonify([item.to_dict() for item in app.categories]), 200
