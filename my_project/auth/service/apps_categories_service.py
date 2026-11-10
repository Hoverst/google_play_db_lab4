from flask import abort
from my_project.auth.dao import apps_categories_dao
from my_project.utils.resource_update import prepare_update

def get_all():
    return [instance.to_dict() for instance in apps_categories_dao.find_all()]

def get_by_id(app_id, category_id):
    instance = apps_categories_dao.find_by_id(app_id, category_id)
    if instance is None:
        abort(404)
    return instance.to_dict()

def create(data):
    required_fields = ['app_id', 'category_id']
    for field in required_fields:
        if field not in data:
            abort(400, description=f"Missing required field: {field}")
    instance = apps_categories_dao.create(data)
    return instance.to_dict()

def update(app_id, category_id, data, partial=False):
    instance = apps_categories_dao.find_by_id(app_id, category_id)
    if instance is None:
        abort(404)
    clean = prepare_update('apps_categories', data, partial=partial)
    instance = apps_categories_dao.update(instance, clean)
    return instance.to_dict()

def delete(app_id, category_id):
    instance = apps_categories_dao.find_by_id(app_id, category_id)
    if instance is None:
        abort(404)
    apps_categories_dao.delete(instance)
