"""Controller for apps_discounts CRUD operations and relationship endpoints."""

from flask import request, jsonify, abort
from sqlalchemy.exc import IntegrityError
from my_project import db
from my_project.auth.domain.apps_discounts import AppDiscount
from my_project.auth.service import apps_discounts_service


def get_all():
    """Return all app discounts."""
    result = apps_discounts_service.get_all()
    return jsonify(result), 200


def get_by_id(discount_id):
    """Return a single app discount by ID."""
    result = apps_discounts_service.get_by_id(discount_id)
    return jsonify(result), 200


def create():
    """Create a new app discount."""
    data = request.get_json()
    if not data:
        return jsonify({"error": "No input data provided"}), 400
    try:
        result = apps_discounts_service.create(data)
        return jsonify(result), 201
    except IntegrityError as e:
        db.session.rollback()
        return jsonify({"error": "Integrity constraint violated: " + str(e.orig)}), 409


def update(discount_id):
    """Update an existing app discount."""
    data = request.get_json()
    if not data:
        return jsonify({"error": "No input data provided"}), 400
    try:
        result = apps_discounts_service.update(discount_id, data)
        return jsonify(result), 200
    except IntegrityError as e:
        db.session.rollback()
        return jsonify({"error": "Integrity constraint violated: " + str(e.orig)}), 409


def delete(discount_id):
    """Delete an app discount by ID."""
    try:
        apps_discounts_service.delete(discount_id)
        return "", 204
    except IntegrityError as e:
        db.session.rollback()
        return jsonify({"error": "Integrity constraint violated: " + str(e.orig)}), 409


# --- Relationship endpoints ---

def get_bills(discount_id):
    """Return all bills that used a given discount."""
    discount = AppDiscount.query.get(discount_id)
    if discount is None:
        abort(404)
    return jsonify([item.to_dict() for item in discount.bills]), 200
