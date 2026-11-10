from flask import abort
from my_project.auth.dao import categories_dao
from my_project.utils.resource_update import prepare_update

def get_all():
    return [instance.to_dict() for instance in categories_dao.find_all()]

def get_by_id(id):
    instance = categories_dao.find_by_id(id)
    if instance is None:
        abort(404)
    return instance.to_dict()

def create(data):
    required_fields = ['name']
    for field in required_fields:
        if field not in data:
            abort(400, description=f"Missing required field: {field}")
    instance = categories_dao.create(data)
    return instance.to_dict()

def update(id, data, partial=False):
    instance = categories_dao.find_by_id(id)
    if instance is None:
        abort(404)
    clean = prepare_update('categories', data, partial=partial)
    instance = categories_dao.update(instance, clean)
    return instance.to_dict()

def delete(id):
    instance = categories_dao.find_by_id(id)
    if instance is None:
        abort(404)
    categories_dao.delete(instance)
