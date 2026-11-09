"""Controller for installations CRUD operations (composite PK)."""

from flask import request, jsonify
from sqlalchemy.exc import IntegrityError
from my_project import db
from my_project.auth.service import installations_service


def get_all():
    """Return all installations."""
    result = installations_service.get_all()
    return jsonify(result), 200


def get_by_id(app_id, device_id):
    """Return a single installation by composite key."""
    result = installations_service.get_by_id(app_id, device_id)
    return jsonify(result), 200


def create():
    """Create a new installation."""
    data = request.get_json()
    if not data:
        return jsonify({"error": "No input data provided"}), 400
    try:
        result = installations_service.create(data)
        return jsonify(result), 201
    except IntegrityError as e:
        db.session.rollback()
        return jsonify({"error": "Integrity constraint violated: " + str(e.orig)}), 409


def update(app_id, device_id):
    """Update an existing installation."""
    data = request.get_json()
    if not data:
        return jsonify({"error": "No input data provided"}), 400
    try:
        result = installations_service.update(app_id, device_id, data)
        return jsonify(result), 200
    except IntegrityError as e:
        db.session.rollback()
        return jsonify({"error": "Integrity constraint violated: " + str(e.orig)}), 409


def delete(app_id, device_id):
    """Delete an installation by composite key."""
    try:
        installations_service.delete(app_id, device_id)
        return "", 204
    except IntegrityError as e:
        db.session.rollback()
        return jsonify({"error": "Integrity constraint violated: " + str(e.orig)}), 409
