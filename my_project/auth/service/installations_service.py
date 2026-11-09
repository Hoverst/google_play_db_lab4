"""Service layer for the installations table (composite PK)."""

from flask import abort
from my_project.auth.dao import installations_dao


def get_all():
    """Return all installation records as a list of dicts."""
    return [instance.to_dict() for instance in installations_dao.find_all()]


def get_by_id(app_id, device_id):
    """Return a single installation dict by composite key, or abort 404."""
    instance = installations_dao.find_by_id(app_id, device_id)
    if instance is None:
        abort(404)
    return instance.to_dict()


def create(data):
    """Validate required fields, create a new installation record, and return its dict."""
    required_fields = ['app_id', 'device_id', 'installed_at']
    for field in required_fields:
        if field not in data:
            abort(400, description=f"Missing required field: {field}")
    instance = installations_dao.create(data)
    return instance.to_dict()


def update(app_id, device_id, data):
    """Update an existing installation record and return its dict, or abort 404."""
    instance = installations_dao.find_by_id(app_id, device_id)
    if instance is None:
        abort(404)
    instance = installations_dao.update(instance, data)
    return instance.to_dict()


def delete(app_id, device_id):
    """Delete an installation record by composite key, or abort 404."""
    instance = installations_dao.find_by_id(app_id, device_id)
    if instance is None:
        abort(404)
    installations_dao.delete(instance)
