from flask import abort
from my_project.auth.dao import apps_discounts_dao
from my_project.utils.resource_update import prepare_update

def get_all():
    return [instance.to_dict() for instance in apps_discounts_dao.find_all()]

def get_by_id(id):
    instance = apps_discounts_dao.find_by_id(id)
    if instance is None:
        abort(404)
    return instance.to_dict()

def create(data):
    required_fields = ['app_id', 'discount_price', 'ends_at']
    for field in required_fields:
        if field not in data:
            abort(400, description=f"Missing required field: {field}")
    instance = apps_discounts_dao.create(data)
    return instance.to_dict()

def update(id, data, partial=False):
    instance = apps_discounts_dao.find_by_id(id)
    if instance is None:
        abort(404)
    clean = prepare_update('apps_discounts', data, partial=partial)
    instance = apps_discounts_dao.update(instance, clean)
    return instance.to_dict()

def delete(id):
    instance = apps_discounts_dao.find_by_id(id)
    if instance is None:
        abort(404)
    apps_discounts_dao.delete(instance)
