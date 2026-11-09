"""Service layer for the apps_discounts table."""

from flask import abort
from my_project.auth.dao import apps_discounts_dao


def get_all():
    """Return all app discounts as a list of dicts."""
    return [instance.to_dict() for instance in apps_discounts_dao.find_all()]


def get_by_id(id):
    """Return a single app discount dict by primary key, or abort 404."""
    instance = apps_discounts_dao.find_by_id(id)
    if instance is None:
        abort(404)
    return instance.to_dict()


def create(data):
    """Validate required fields, create a new app discount, and return its dict."""
    required_fields = ['app_id', 'discount_price', 'starts_at', 'ends_at']
    for field in required_fields:
        if field not in data:
            abort(400, description=f"Missing required field: {field}")
    instance = apps_discounts_dao.create(data)
    return instance.to_dict()


def update(id, data):
    """Update an existing app discount by id and return its dict, or abort 404."""
    instance = apps_discounts_dao.find_by_id(id)
    if instance is None:
        abort(404)
    instance = apps_discounts_dao.update(instance, data)
    return instance.to_dict()


def delete(id):
    """Delete an app discount by id, or abort 404."""
    instance = apps_discounts_dao.find_by_id(id)
    if instance is None:
        abort(404)
    apps_discounts_dao.delete(instance)
