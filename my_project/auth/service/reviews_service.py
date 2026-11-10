from flask import abort
from my_project.auth.dao import reviews_dao
from my_project.utils.resource_update import prepare_update

def get_all():
    return [instance.to_dict() for instance in reviews_dao.find_all()]

def get_by_id(account_id, app_id):
    instance = reviews_dao.find_by_id(account_id, app_id)
    if instance is None:
        abort(404)
    return instance.to_dict()

def create(data):
    required_fields = ['account_id', 'app_id', 'rating']
    for field in required_fields:
        if field not in data:
            abort(400, description=f"Missing required field: {field}")
    instance = reviews_dao.create(data)
    return instance.to_dict()

def update(account_id, app_id, data, partial=False):
    instance = reviews_dao.find_by_id(account_id, app_id)
    if instance is None:
        abort(404)
    clean = prepare_update('reviews', data, partial=partial)
    instance = reviews_dao.update(instance, clean)
    return instance.to_dict()

def delete(account_id, app_id):
    instance = reviews_dao.find_by_id(account_id, app_id)
    if instance is None:
        abort(404)
    reviews_dao.delete(instance)
