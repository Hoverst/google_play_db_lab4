from flask import abort
from my_project.auth.dao import devices_dao
from my_project.utils.resource_update import prepare_update

def get_all():
    return [instance.to_dict() for instance in devices_dao.find_all()]

def get_by_id(id):
    instance = devices_dao.find_by_id(id)
    if instance is None:
        abort(404)
    return instance.to_dict()

def create(data):
    required_fields = ['model', 'os_version']
    for field in required_fields:
        if field not in data:
            abort(400, description=f"Missing required field: {field}")
    instance = devices_dao.create(data)
    return instance.to_dict()

def update(id, data, partial=False):
    instance = devices_dao.find_by_id(id)
    if instance is None:
        abort(404)
    clean = prepare_update('devices', data, partial=partial)
    instance = devices_dao.update(instance, clean)
    return instance.to_dict()

def delete(id):
    instance = devices_dao.find_by_id(id)
    if instance is None:
        abort(404)
    devices_dao.delete(instance)
