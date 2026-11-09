"""Controller for apps_versions CRUD operations."""

from flask import request, jsonify
from sqlalchemy.exc import IntegrityError
from my_project import db
from my_project.auth.service import apps_versions_service


def get_all():
    """Return all app versions."""
    result = apps_versions_service.get_all()
    return jsonify(result), 200


def get_by_id(version_id):
    """Return a single app version by ID."""
    result = apps_versions_service.get_by_id(version_id)
    return jsonify(result), 200


def create():
    """Create a new app version."""
    data = request.get_json()
    if not data:
        return jsonify({"error": "No input data provided"}), 400
    try:
        result = apps_versions_service.create(data)
        return jsonify(result), 201
    except IntegrityError as e:
        db.session.rollback()
        return jsonify({"error": "Integrity constraint violated: " + str(e.orig)}), 409


def update(version_id):
    """Update an existing app version."""
    data = request.get_json()
    if not data:
        return jsonify({"error": "No input data provided"}), 400
    try:
        result = apps_versions_service.update(version_id, data)
        return jsonify(result), 200
    except IntegrityError as e:
        db.session.rollback()
        return jsonify({"error": "Integrity constraint violated: " + str(e.orig)}), 409


def delete(version_id):
    """Delete an app version by ID."""
    try:
        apps_versions_service.delete(version_id)
        return "", 204
    except IntegrityError as e:
        db.session.rollback()
        return jsonify({"error": "Integrity constraint violated: " + str(e.orig)}), 409
