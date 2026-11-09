"""Controller for apps CRUD operations and relationship endpoints."""

from flask import request, jsonify, abort
from sqlalchemy.exc import IntegrityError
from my_project import db
from my_project.auth.domain.apps import App
from my_project.auth.service import apps_service


def get_all():
    """Return all apps."""
    result = apps_service.get_all()
    return jsonify(result), 200


def get_by_id(app_id):
    """Return a single app by ID."""
    result = apps_service.get_by_id(app_id)
    return jsonify(result), 200


def create():
    """Create a new app."""
    data = request.get_json()
    if not data:
        return jsonify({"error": "No input data provided"}), 400
    try:
        result = apps_service.create(data)
        return jsonify(result), 201
    except IntegrityError as e:
        db.session.rollback()
        return jsonify({"error": "Integrity constraint violated: " + str(e.orig)}), 409


def update(app_id):
    """Update an existing app."""
    data = request.get_json()
    if not data:
        return jsonify({"error": "No input data provided"}), 400
    try:
        result = apps_service.update(app_id, data)
        return jsonify(result), 200
    except IntegrityError as e:
        db.session.rollback()
        return jsonify({"error": "Integrity constraint violated: " + str(e.orig)}), 409


def delete(app_id):
    """Delete an app by ID."""
    try:
        apps_service.delete(app_id)
        return "", 204
    except IntegrityError as e:
        db.session.rollback()
        return jsonify({"error": "Integrity constraint violated: " + str(e.orig)}), 409


# --- Relationship endpoints ---

def get_versions(app_id):
    """Return all versions for a given app."""
    app = App.query.get(app_id)
    if app is None:
        abort(404)
    return jsonify([item.to_dict() for item in app.versions]), 200


def get_discounts(app_id):
    """Return all discounts for a given app."""
    app = App.query.get(app_id)
    if app is None:
        abort(404)
    return jsonify([item.to_dict() for item in app.discounts]), 200


def get_reviews(app_id):
    """Return all reviews for a given app."""
    app = App.query.get(app_id)
    if app is None:
        abort(404)
    return jsonify([item.to_dict() for item in app.reviews]), 200


def get_bills(app_id):
    """Return all bills for a given app."""
    app = App.query.get(app_id)
    if app is None:
        abort(404)
    return jsonify([item.to_dict() for item in app.bills]), 200


def get_library(app_id):
    """Return all library entries for a given app."""
    app = App.query.get(app_id)
    if app is None:
        abort(404)
    return jsonify([item.to_dict() for item in app.library_entries]), 200


def get_installations(app_id):
    """Return all installations for a given app."""
    app = App.query.get(app_id)
    if app is None:
        abort(404)
    return jsonify([item.to_dict() for item in app.installations]), 200


def get_categories(app_id):
    """Return all categories for a given app (M:M through apps_categories)."""
    app = App.query.get(app_id)
    if app is None:
        abort(404)
    return jsonify([item.to_dict() for item in app.categories]), 200
