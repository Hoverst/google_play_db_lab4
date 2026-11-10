from flask import abort
from my_project.auth.dao import library_dao
from my_project.utils.resource_update import prepare_update

def get_all():
    return [instance.to_dict() for instance in library_dao.find_all()]

def get_by_id(app_id, account_id):
    instance = library_dao.find_by_id(app_id, account_id)
    if instance is None:
        abort(404)
    return instance.to_dict()

def create(data):
    required_fields = ['app_id', 'account_id']
    for field in required_fields:
        if field not in data:
            abort(400, description=f"Missing required field: {field}")
    instance = library_dao.create(data)
    return instance.to_dict()

def update(app_id, account_id, data, partial=False):
    instance = library_dao.find_by_id(app_id, account_id)
    if instance is None:
        abort(404)
    clean = prepare_update('library', data, partial=partial)
    instance = library_dao.update(instance, clean)
    return instance.to_dict()

def delete(app_id, account_id):
    instance = library_dao.find_by_id(app_id, account_id)
    if instance is None:
        abort(404)
    library_dao.delete(instance)
