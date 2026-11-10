from flask import abort
from my_project.auth.dao import installations_dao
from my_project.utils.resource_update import prepare_update

def get_all():
    return [instance.to_dict() for instance in installations_dao.find_all()]

def get_by_id(app_id, device_id):
    instance = installations_dao.find_by_id(app_id, device_id)
    if instance is None:
        abort(404)
    return instance.to_dict()

def create(data):
    required_fields = ['app_id', 'device_id']
    for field in required_fields:
        if field not in data:
            abort(400, description=f"Missing required field: {field}")
    instance = installations_dao.create(data)
    return instance.to_dict()

def update(app_id, device_id, data, partial=False):
    instance = installations_dao.find_by_id(app_id, device_id)
    if instance is None:
        abort(404)
    clean = prepare_update('installations', data, partial=partial)
    instance = installations_dao.update(instance, clean)
    return instance.to_dict()

def delete(app_id, device_id):
    instance = installations_dao.find_by_id(app_id, device_id)
    if instance is None:
        abort(404)
    installations_dao.delete(instance)
