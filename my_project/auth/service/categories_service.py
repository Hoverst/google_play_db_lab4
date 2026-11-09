"""Service layer for the categories table."""

from flask import abort
from my_project.auth.dao import categories_dao


def get_all():
    """Return all categories as a list of dicts."""
    return [instance.to_dict() for instance in categories_dao.find_all()]


def get_by_id(id):
    """Return a single category dict by primary key, or abort 404."""
    instance = categories_dao.find_by_id(id)
    if instance is None:
        abort(404)
    return instance.to_dict()


def create(data):
    """Validate required fields, create a new category, and return its dict."""
    required_fields = ['name']
    for field in required_fields:
        if field not in data:
            abort(400, description=f"Missing required field: {field}")
    instance = categories_dao.create(data)
    return instance.to_dict()


def update(id, data):
    """Update an existing category by id and return its dict, or abort 404."""
    instance = categories_dao.find_by_id(id)
    if instance is None:
        abort(404)
    instance = categories_dao.update(instance, data)
    return instance.to_dict()


def delete(id):
    """Delete a category by id, or abort 404."""
    instance = categories_dao.find_by_id(id)
    if instance is None:
        abort(404)
    categories_dao.delete(instance)
