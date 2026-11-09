"""Service layer for the reviews table (composite PK)."""

from flask import abort
from my_project.auth.dao import reviews_dao


def get_all():
    """Return all reviews as a list of dicts."""
    return [instance.to_dict() for instance in reviews_dao.find_all()]


def get_by_id(account_id, app_id):
    """Return a single review dict by composite key, or abort 404."""
    instance = reviews_dao.find_by_id(account_id, app_id)
    if instance is None:
        abort(404)
    return instance.to_dict()


def create(data):
    """Validate required fields, create a new review, and return its dict."""
    required_fields = ['account_id', 'app_id', 'rating', 'created_at']
    for field in required_fields:
        if field not in data:
            abort(400, description=f"Missing required field: {field}")
    instance = reviews_dao.create(data)
    return instance.to_dict()


def update(account_id, app_id, data):
    """Update an existing review and return its dict, or abort 404."""
    instance = reviews_dao.find_by_id(account_id, app_id)
    if instance is None:
        abort(404)
    instance = reviews_dao.update(instance, data)
    return instance.to_dict()


def delete(account_id, app_id):
    """Delete a review by composite key, or abort 404."""
    instance = reviews_dao.find_by_id(account_id, app_id)
    if instance is None:
        abort(404)
    reviews_dao.delete(instance)
