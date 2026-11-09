"""Controller for apps_categories CRUD operations (composite PK)."""

from flask import request, jsonify
from sqlalchemy.exc import IntegrityError
from my_project import db
from my_project.auth.service import apps_categories_service


def get_all():
    """Return all apps_categories records."""
    result = apps_categories_service.get_all()
    return jsonify(result), 200


def get_by_id(app_id, category_id):
    """Return a single apps_categories record by composite key."""
    result = apps_categories_service.get_by_id(app_id, category_id)
    return jsonify(result), 200


def create():
    """Create a new apps_categories record."""
    data = request.get_json()
    if not data:
        return jsonify({"error": "No input data provided"}), 400
    try:
        result = apps_categories_service.create(data)
        return jsonify(result), 201
    except IntegrityError as e:
        db.session.rollback()
        return jsonify({"error": "Integrity constraint violated: " + str(e.orig)}), 409


def update(app_id, category_id):
    """Update an existing apps_categories record."""
    data = request.get_json()
    if not data:
        return jsonify({"error": "No input data provided"}), 400
    try:
        result = apps_categories_service.update(app_id, category_id, data)
        return jsonify(result), 200
    except IntegrityError as e:
        db.session.rollback()
        return jsonify({"error": "Integrity constraint violated: " + str(e.orig)}), 409


def delete(app_id, category_id):
    """Delete an apps_categories record by composite key."""
    try:
        apps_categories_service.delete(app_id, category_id)
        return "", 204
    except IntegrityError as e:
        db.session.rollback()
        return jsonify({"error": "Integrity constraint violated: " + str(e.orig)}), 409
