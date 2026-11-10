from flask import abort
from my_project.auth.dao import companies_dao
from my_project.utils.resource_update import prepare_update

def get_all():
    return [instance.to_dict() for instance in companies_dao.find_all()]

def get_by_id(id):
    instance = companies_dao.find_by_id(id)
    if instance is None:
        abort(404)
    return instance.to_dict()

def create(data):
    required_fields = ['company_name', 'developer_account_id']
    for field in required_fields:
        if field not in data:
            abort(400, description=f"Missing required field: {field}")
    instance = companies_dao.create(data)
    return instance.to_dict()

def update(id, data, partial=False):
    instance = companies_dao.find_by_id(id)
    if instance is None:
        abort(404)
    clean = prepare_update('companies', data, partial=partial)
    instance = companies_dao.update(instance, clean)
    return instance.to_dict()

def delete(id):
    instance = companies_dao.find_by_id(id)
    if instance is None:
        abort(404)
    companies_dao.delete(instance)
