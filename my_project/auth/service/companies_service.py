from flask import abort
from sqlalchemy.exc import IntegrityError
from my_project.auth.dao import companies_dao, accounts_dao


def get_all():
    return [c.to_dict() for c in companies_dao.find_all()]


def get_by_id(company_id):
    company = companies_dao.find_by_id(company_id)
    if company is None:
        abort(404)
    return company.to_dict()


def get_apps(company_id):
    company = companies_dao.find_by_id(company_id)
    if company is None:
        abort(404)
    return [a.to_dict() for a in company.apps]


def _ensure_developer(developer_id, exclude_company_id=None):
    account = accounts_dao.find_by_id_active(developer_id)
    if account is None:
        abort(400, description="developer_id must reference an existing non-deleted account")
    if companies_dao.find_by_developer_id(developer_id, exclude_company_id=exclude_company_id) is not None:
        abort(409, description="Account already owns a company")


def create(data):
    _ensure_developer(data["developer_id"])
    try:
        company = companies_dao.create(data)
    except IntegrityError:
        abort(409, description="Company name or developer already taken")
    return company.to_dict()


def update(company_id, data, partial=False):
    company = companies_dao.find_by_id(company_id)
    if company is None:
        abort(404)
    if "developer_id" in data:
        _ensure_developer(data["developer_id"], exclude_company_id=company_id)
    try:
        company = companies_dao.update(company, data)
    except IntegrityError:
        abort(409, description="Company name or developer already taken")
    return company.to_dict()


def delete(company_id):
    company = companies_dao.find_by_id(company_id)
    if company is None:
        abort(404)
    if company.apps:
        abort(409, description="Cannot delete company that still has apps")
    try:
        companies_dao.delete(company)
    except IntegrityError:
        abort(409, description="Cannot delete company due to related records")
