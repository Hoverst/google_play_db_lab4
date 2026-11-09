"""Controller for reviews CRUD operations (composite PK)."""

from flask import request, jsonify
from sqlalchemy.exc import IntegrityError
from my_project import db
from my_project.auth.service import reviews_service


def get_all():
    """Return all reviews."""
    result = reviews_service.get_all()
    return jsonify(result), 200


def get_by_id(account_id, app_id):
    """Return a single review by composite key."""
    result = reviews_service.get_by_id(account_id, app_id)
    return jsonify(result), 200


def create():
    """Create a new review."""
    data = request.get_json()
    if not data:
        return jsonify({"error": "No input data provided"}), 400
    try:
        result = reviews_service.create(data)
        return jsonify(result), 201
    except IntegrityError as e:
        db.session.rollback()
        return jsonify({"error": "Integrity constraint violated: " + str(e.orig)}), 409


def update(account_id, app_id):
    """Update an existing review."""
    data = request.get_json()
    if not data:
        return jsonify({"error": "No input data provided"}), 400
    try:
        result = reviews_service.update(account_id, app_id, data)
        return jsonify(result), 200
    except IntegrityError as e:
        db.session.rollback()
        return jsonify({"error": "Integrity constraint violated: " + str(e.orig)}), 409


def delete(account_id, app_id):
    """Delete a review by composite key."""
    try:
        reviews_service.delete(account_id, app_id)
        return "", 204
    except IntegrityError as e:
        db.session.rollback()
        return jsonify({"error": "Integrity constraint violated: " + str(e.orig)}), 409
