"""Service layer for the library table (composite PK)."""

from flask import abort
from my_project.auth.dao import library_dao


def get_all():
    """Return all library records as a list of dicts."""
    return [instance.to_dict() for instance in library_dao.find_all()]


def get_by_id(app_id, account_id):
    """Return a single library dict by composite key, or abort 404."""
    instance = library_dao.find_by_id(app_id, account_id)
    if instance is None:
        abort(404)
    return instance.to_dict()


def create(data):
    """Validate required fields, create a new library record, and return its dict."""
    required_fields = ['app_id', 'account_id']
    for field in required_fields:
        if field not in data:
            abort(400, description=f"Missing required field: {field}")
    instance = library_dao.create(data)
    return instance.to_dict()


def update(app_id, account_id, data):
    """Update an existing library record and return its dict, or abort 404."""
    instance = library_dao.find_by_id(app_id, account_id)
    if instance is None:
        abort(404)
    instance = library_dao.update(instance, data)
    return instance.to_dict()


def delete(app_id, account_id):
    """Delete a library record by composite key, or abort 404."""
    instance = library_dao.find_by_id(app_id, account_id)
    if instance is None:
        abort(404)
    library_dao.delete(instance)
