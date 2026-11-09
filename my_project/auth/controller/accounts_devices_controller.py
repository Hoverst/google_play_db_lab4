"""Controller for accounts_devices CRUD operations (composite PK)."""

from flask import request, jsonify
from sqlalchemy.exc import IntegrityError
from my_project import db
from my_project.auth.service import accounts_devices_service


def get_all():
    """Return all accounts_devices records."""
    result = accounts_devices_service.get_all()
    return jsonify(result), 200


def get_by_id(account_id, device_id):
    """Return a single accounts_devices record by composite key."""
    result = accounts_devices_service.get_by_id(account_id, device_id)
    return jsonify(result), 200


def create():
    """Create a new accounts_devices record."""
    data = request.get_json()
    if not data:
        return jsonify({"error": "No input data provided"}), 400
    try:
        result = accounts_devices_service.create(data)
        return jsonify(result), 201
    except IntegrityError as e:
        db.session.rollback()
        return jsonify({"error": "Integrity constraint violated: " + str(e.orig)}), 409


def update(account_id, device_id):
    """Update an existing accounts_devices record."""
    data = request.get_json()
    if not data:
        return jsonify({"error": "No input data provided"}), 400
    try:
        result = accounts_devices_service.update(account_id, device_id, data)
        return jsonify(result), 200
    except IntegrityError as e:
        db.session.rollback()
        return jsonify({"error": "Integrity constraint violated: " + str(e.orig)}), 409


def delete(account_id, device_id):
    """Delete an accounts_devices record by composite key."""
    try:
        accounts_devices_service.delete(account_id, device_id)
        return "", 204
    except IntegrityError as e:
        db.session.rollback()
        return jsonify({"error": "Integrity constraint violated: " + str(e.orig)}), 409
