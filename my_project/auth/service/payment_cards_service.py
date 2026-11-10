from flask import abort
from my_project.auth.dao import payment_cards_dao
from my_project.utils.resource_update import prepare_update

def get_all():
    return [instance.to_dict() for instance in payment_cards_dao.find_all()]

def get_by_id(id):
    instance = payment_cards_dao.find_by_id(id)
    if instance is None:
        abort(404)
    return instance.to_dict()

def create(data):
    required_fields = ['account_id', 'token', 'card_brand', 'exp_date', 'last4']
    for field in required_fields:
        if field not in data:
            abort(400, description=f"Missing required field: {field}")
    instance = payment_cards_dao.create(data)
    return instance.to_dict()

def update(id, data, partial=False):
    instance = payment_cards_dao.find_by_id(id)
    if instance is None:
        abort(404)
    clean = prepare_update('payment_cards', data, partial=partial)
    instance = payment_cards_dao.update(instance, clean)
    return instance.to_dict()

def delete(id):
    instance = payment_cards_dao.find_by_id(id)
    if instance is None:
        abort(404)
    payment_cards_dao.delete(instance)
