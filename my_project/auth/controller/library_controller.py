"""Controller for library CRUD operations (composite PK)."""

from flask import request, jsonify
from sqlalchemy.exc import IntegrityError
from my_project import db
from my_project.auth.service import library_service


def get_all():
    """Return all library records."""
    result = library_service.get_all()
    return jsonify(result), 200


def get_by_id(app_id, account_id):
    """Return a single library record by composite key."""
    result = library_service.get_by_id(app_id, account_id)
    return jsonify(result), 200


def create():
    """Create a new library record."""
    data = request.get_json()
    if not data:
        return jsonify({"error": "No input data provided"}), 400
    try:
        result = library_service.create(data)
        return jsonify(result), 201
    except IntegrityError as e:
        db.session.rollback()
        return jsonify({"error": "Integrity constraint violated: " + str(e.orig)}), 409


def update(app_id, account_id):
    """Update an existing library record."""
    data = request.get_json()
    if not data:
        return jsonify({"error": "No input data provided"}), 400
    try:
        result = library_service.update(app_id, account_id, data)
        return jsonify(result), 200
    except IntegrityError as e:
        db.session.rollback()
        return jsonify({"error": "Integrity constraint violated: " + str(e.orig)}), 409


def delete(app_id, account_id):
    """Delete a library record by composite key."""
    try:
        library_service.delete(app_id, account_id)
        return "", 204
    except IntegrityError as e:
        db.session.rollback()
        return jsonify({"error": "Integrity constraint violated: " + str(e.orig)}), 409
