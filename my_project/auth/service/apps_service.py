"""Service layer for the apps table."""

from flask import abort
from my_project.auth.dao import apps_dao


def get_all():
    """Return all apps as a list of dicts."""
    return [instance.to_dict() for instance in apps_dao.find_all()]


def get_by_id(id):
    """Return a single app dict by primary key, or abort 404."""
    instance = apps_dao.find_by_id(id)
    if instance is None:
        abort(404)
    return instance.to_dict()


def create(data):
    """Validate required fields, create a new app, and return its dict."""
    required_fields = ['title', 'company_id']
    for field in required_fields:
        if field not in data:
            abort(400, description=f"Missing required field: {field}")
    instance = apps_dao.create(data)
    return instance.to_dict()


def update(id, data):
    """Update an existing app by id and return its dict, or abort 404."""
    instance = apps_dao.find_by_id(id)
    if instance is None:
        abort(404)
    instance = apps_dao.update(instance, data)
    return instance.to_dict()


def delete(id):
    """Delete an app by id, or abort 404."""
    instance = apps_dao.find_by_id(id)
    if instance is None:
        abort(404)
    apps_dao.delete(instance)
