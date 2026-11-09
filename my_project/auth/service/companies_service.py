"""Service layer for the companies table."""

from flask import abort
from my_project.auth.dao import companies_dao


def get_all():
    """Return all companies as a list of dicts."""
    return [instance.to_dict() for instance in companies_dao.find_all()]


def get_by_id(id):
    """Return a single company dict by primary key, or abort 404."""
    instance = companies_dao.find_by_id(id)
    if instance is None:
        abort(404)
    return instance.to_dict()


def create(data):
    """Validate required fields, create a new company, and return its dict."""
    required_fields = ['company_name', 'developer_account_id']
    for field in required_fields:
        if field not in data:
            abort(400, description=f"Missing required field: {field}")
    instance = companies_dao.create(data)
    return instance.to_dict()


def update(id, data):
    """Update an existing company by id and return its dict, or abort 404."""
    instance = companies_dao.find_by_id(id)
    if instance is None:
        abort(404)
    instance = companies_dao.update(instance, data)
    return instance.to_dict()


def delete(id):
    """Delete a company by id, or abort 404."""
    instance = companies_dao.find_by_id(id)
    if instance is None:
        abort(404)
    companies_dao.delete(instance)
