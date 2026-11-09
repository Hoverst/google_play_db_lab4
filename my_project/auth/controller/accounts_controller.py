"""Controller for accounts CRUD operations and relationship endpoints."""

from flask import request, jsonify, abort
from sqlalchemy.exc import IntegrityError
from my_project import db
from my_project.auth.domain.accounts import Account
from my_project.auth.service import accounts_service


def get_all():
    """Return all accounts."""
    result = accounts_service.get_all()
    return jsonify(result), 200


def get_by_id(account_id):
    """Return a single account by ID."""
    result = accounts_service.get_by_id(account_id)
    return jsonify(result), 200


def create():
    """Create a new account."""
    data = request.get_json()
    if not data:
        return jsonify({"error": "No input data provided"}), 400
    try:
        result = accounts_service.create(data)
        return jsonify(result), 201
    except IntegrityError as e:
        db.session.rollback()
        return jsonify({"error": "Integrity constraint violated: " + str(e.orig)}), 409


def update(account_id):
    """Update an existing account."""
    data = request.get_json()
    if not data:
        return jsonify({"error": "No input data provided"}), 400
    try:
        result = accounts_service.update(account_id, data)
        return jsonify(result), 200
    except IntegrityError as e:
        db.session.rollback()
        return jsonify({"error": "Integrity constraint violated: " + str(e.orig)}), 409


def delete(account_id):
    """Delete an account by ID."""
    try:
        accounts_service.delete(account_id)
        return "", 204
    except IntegrityError as e:
        db.session.rollback()
        return jsonify({"error": "Integrity constraint violated: " + str(e.orig)}), 409


# --- Relationship endpoints ---

def get_companies(account_id):
    """Return all companies for a given account."""
    account = Account.query.get(account_id)
    if account is None:
        abort(404)
    return jsonify([item.to_dict() for item in account.companies]), 200


def get_payment_cards(account_id):
    """Return all payment cards for a given account."""
    account = Account.query.get(account_id)
    if account is None:
        abort(404)
    return jsonify([item.to_dict() for item in account.payment_cards]), 200


def get_reviews(account_id):
    """Return all reviews by a given account."""
    account = Account.query.get(account_id)
    if account is None:
        abort(404)
    return jsonify([item.to_dict() for item in account.reviews]), 200


def get_bills(account_id):
    """Return all bills for a given account."""
    account = Account.query.get(account_id)
    if account is None:
        abort(404)
    return jsonify([item.to_dict() for item in account.bills]), 200


def get_library(account_id):
    """Return all library entries for a given account."""
    account = Account.query.get(account_id)
    if account is None:
        abort(404)
    return jsonify([item.to_dict() for item in account.library_entries]), 200


def get_devices(account_id):
    """Return all devices for a given account (M:M through accounts_devices)."""
    account = Account.query.get(account_id)
    if account is None:
        abort(404)
    return jsonify([item.to_dict() for item in account.devices]), 200
