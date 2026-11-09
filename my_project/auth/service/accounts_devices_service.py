"""Service layer for the accounts_devices table (composite PK)."""

from flask import abort
from my_project.auth.dao import accounts_devices_dao


def get_all():
    """Return all account-device records as a list of dicts."""
    return [instance.to_dict() for instance in accounts_devices_dao.find_all()]


def get_by_id(account_id, device_id):
    """Return a single account-device dict by composite key, or abort 404."""
    instance = accounts_devices_dao.find_by_id(account_id, device_id)
    if instance is None:
        abort(404)
    return instance.to_dict()


def create(data):
    """Validate required fields, create a new account-device record, and return its dict."""
    required_fields = ['account_id', 'device_id']
    for field in required_fields:
        if field not in data:
            abort(400, description=f"Missing required field: {field}")
    instance = accounts_devices_dao.create(data)
    return instance.to_dict()


def update(account_id, device_id, data):
    """Update an existing account-device record and return its dict, or abort 404."""
    instance = accounts_devices_dao.find_by_id(account_id, device_id)
    if instance is None:
        abort(404)
    instance = accounts_devices_dao.update(instance, data)
    return instance.to_dict()


def delete(account_id, device_id):
    """Delete an account-device record by composite key, or abort 404."""
    instance = accounts_devices_dao.find_by_id(account_id, device_id)
    if instance is None:
        abort(404)
    accounts_devices_dao.delete(instance)
