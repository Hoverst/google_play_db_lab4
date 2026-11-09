"""Service layer for the payment_cards table."""

from flask import abort
from my_project.auth.dao import payment_cards_dao


def get_all():
    """Return all payment cards as a list of dicts."""
    return [instance.to_dict() for instance in payment_cards_dao.find_all()]


def get_by_id(id):
    """Return a single payment card dict by primary key, or abort 404."""
    instance = payment_cards_dao.find_by_id(id)
    if instance is None:
        abort(404)
    return instance.to_dict()


def create(data):
    """Validate required fields, create a new payment card, and return its dict."""
    required_fields = ['account_id', 'token', 'card_brand', 'exp_date', 'last4']
    for field in required_fields:
        if field not in data:
            abort(400, description=f"Missing required field: {field}")
    instance = payment_cards_dao.create(data)
    return instance.to_dict()


def update(id, data):
    """Update an existing payment card by id and return its dict, or abort 404."""
    instance = payment_cards_dao.find_by_id(id)
    if instance is None:
        abort(404)
    instance = payment_cards_dao.update(instance, data)
    return instance.to_dict()


def delete(id):
    """Delete a payment card by id, or abort 404."""
    instance = payment_cards_dao.find_by_id(id)
    if instance is None:
        abort(404)
    payment_cards_dao.delete(instance)
