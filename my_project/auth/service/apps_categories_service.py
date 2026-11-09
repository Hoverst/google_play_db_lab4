"""Service layer for the apps_categories table (composite PK)."""

from flask import abort
from my_project.auth.dao import apps_categories_dao


def get_all():
    """Return all app-category records as a list of dicts."""
    return [instance.to_dict() for instance in apps_categories_dao.find_all()]


def get_by_id(app_id, category_id):
    """Return a single app-category dict by composite key, or abort 404."""
    instance = apps_categories_dao.find_by_id(app_id, category_id)
    if instance is None:
        abort(404)
    return instance.to_dict()


def create(data):
    """Validate required fields, create a new app-category record, and return its dict."""
    required_fields = ['app_id', 'category_id']
    for field in required_fields:
        if field not in data:
            abort(400, description=f"Missing required field: {field}")
    instance = apps_categories_dao.create(data)
    return instance.to_dict()


def update(app_id, category_id, data):
    """Update an existing app-category record and return its dict, or abort 404."""
    instance = apps_categories_dao.find_by_id(app_id, category_id)
    if instance is None:
        abort(404)
    instance = apps_categories_dao.update(instance, data)
    return instance.to_dict()


def delete(app_id, category_id):
    """Delete an app-category record by composite key, or abort 404."""
    instance = apps_categories_dao.find_by_id(app_id, category_id)
    if instance is None:
        abort(404)
    apps_categories_dao.delete(instance)
