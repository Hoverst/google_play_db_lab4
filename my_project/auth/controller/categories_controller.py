"""Controller for categories CRUD operations and relationship endpoints."""

from flask import request, jsonify, abort
from sqlalchemy.exc import IntegrityError
from my_project import db
from my_project.auth.domain.categories import Category
from my_project.auth.service import categories_service


def get_all():
    """Return all categories."""
    result = categories_service.get_all()
    return jsonify(result), 200


def get_by_id(category_id):
    """Return a single category by ID."""
    result = categories_service.get_by_id(category_id)
    return jsonify(result), 200


def create():
    """Create a new category."""
    data = request.get_json()
    if not data:
        return jsonify({"error": "No input data provided"}), 400
    try:
        result = categories_service.create(data)
        return jsonify(result), 201
    except IntegrityError as e:
        db.session.rollback()
        return jsonify({"error": "Integrity constraint violated: " + str(e.orig)}), 409


def update(category_id):
    """Update an existing category."""
    data = request.get_json()
    if not data:
        return jsonify({"error": "No input data provided"}), 400
    try:
        result = categories_service.update(category_id, data)
        return jsonify(result), 200
    except IntegrityError as e:
        db.session.rollback()
        return jsonify({"error": "Integrity constraint violated: " + str(e.orig)}), 409


def delete(category_id):
    """Delete a category by ID."""
    try:
        categories_service.delete(category_id)
        return "", 204
    except IntegrityError as e:
        db.session.rollback()
        return jsonify({"error": "Integrity constraint violated: " + str(e.orig)}), 409


# --- Relationship endpoints ---

def get_apps(category_id):
    """Return all apps for a given category (M:M through apps_categories)."""
    category = Category.query.get(category_id)
    if category is None:
        abort(404)
    return jsonify([item.to_dict() for item in category.apps]), 200
