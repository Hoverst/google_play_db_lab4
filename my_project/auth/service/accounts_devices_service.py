from flask import abort
from my_project.auth.dao import accounts_devices_dao
from my_project.utils.resource_update import prepare_update

def get_all():
    return [instance.to_dict() for instance in accounts_devices_dao.find_all()]

def get_by_id(account_id, device_id):
    instance = accounts_devices_dao.find_by_id(account_id, device_id)
    if instance is None:
        abort(404)
    return instance.to_dict()

def create(data):
    required_fields = ['account_id', 'device_id']
    for field in required_fields:
        if field not in data:
            abort(400, description=f"Missing required field: {field}")
    instance = accounts_devices_dao.create(data)
    return instance.to_dict()

def update(account_id, device_id, data, partial=False):
    instance = accounts_devices_dao.find_by_id(account_id, device_id)
    if instance is None:
        abort(404)
    clean = prepare_update('accounts_devices', data, partial=partial)
    instance = accounts_devices_dao.update(instance, clean)
    return instance.to_dict()

def delete(account_id, device_id):
    instance = accounts_devices_dao.find_by_id(account_id, device_id)
    if instance is None:
        abort(404)
    accounts_devices_dao.delete(instance)
