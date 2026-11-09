"""Service layer for the bills table (composite PK)."""

from flask import abort
from my_project.auth.dao import bills_dao


def get_all():
    """Return all bills as a list of dicts."""
    return [instance.to_dict() for instance in bills_dao.find_all()]


def get_by_id(account_id, app_id):
    """Return a single bill dict by composite key, or abort 404."""
    instance = bills_dao.find_by_id(account_id, app_id)
    if instance is None:
        abort(404)
    return instance.to_dict()


def create(data):
    """Validate required fields, create a new bill, and return its dict."""
    required_fields = ['account_id', 'app_id', 'amount_paid', 'payment_card_id', 'paid_at']
    for field in required_fields:
        if field not in data:
            abort(400, description=f"Missing required field: {field}")
    instance = bills_dao.create(data)
    return instance.to_dict()


def update(account_id, app_id, data):
    """Update an existing bill and return its dict, or abort 404."""
    instance = bills_dao.find_by_id(account_id, app_id)
    if instance is None:
        abort(404)
    instance = bills_dao.update(instance, data)
    return instance.to_dict()


def delete(account_id, app_id):
    """Delete a bill by composite key, or abort 404."""
    instance = bills_dao.find_by_id(account_id, app_id)
    if instance is None:
        abort(404)
    bills_dao.delete(instance)
