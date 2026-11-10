from flask import abort
from my_project.auth.dao import bills_dao
from my_project.utils.resource_update import prepare_update

def get_all():
    return [instance.to_dict() for instance in bills_dao.find_all()]

def get_by_id(account_id, app_id):
    instance = bills_dao.find_by_id(account_id, app_id)
    if instance is None:
        abort(404)
    return instance.to_dict()

def create(data):
    required_fields = ['account_id', 'app_id', 'amount_paid', 'payment_card_id']
    for field in required_fields:
        if field not in data:
            abort(400, description=f"Missing required field: {field}")
    instance = bills_dao.create(data)
    return instance.to_dict()

def update(account_id, app_id, data, partial=False):
    instance = bills_dao.find_by_id(account_id, app_id)
    if instance is None:
        abort(404)
    clean = prepare_update('bills', data, partial=partial)
    instance = bills_dao.update(instance, clean)
    return instance.to_dict()

def delete(account_id, app_id):
    instance = bills_dao.find_by_id(account_id, app_id)
    if instance is None:
        abort(404)
    bills_dao.delete(instance)
