"""Service layer for the accounts table."""

from flask import abort
from my_project.auth.dao import accounts_dao


def get_all():
    """Return all accounts as a list of dicts."""
    return [instance.to_dict() for instance in accounts_dao.find_all()]


def get_by_id(id):
    """Return a single account dict by primary key, or abort 404."""
    instance = accounts_dao.find_by_id(id)
    if instance is None:
        abort(404)
    return instance.to_dict()


def create(data):
    """Validate required fields, create a new account, and return its dict."""
    required_fields = ['email', 'password_hash', 'name', 'country', 'created_at']
    for field in required_fields:
        if field not in data:
            abort(400, description=f"Missing required field: {field}")
    instance = accounts_dao.create(data)
    return instance.to_dict()


def update(id, data):
    """Update an existing account by id and return its dict, or abort 404."""
    instance = accounts_dao.find_by_id(id)
    if instance is None:
        abort(404)
    instance = accounts_dao.update(instance, data)
    return instance.to_dict()


def delete(id):
    """Delete an account by id, or abort 404."""
    instance = accounts_dao.find_by_id(id)
    if instance is None:
        abort(404)
    accounts_dao.delete(instance)
