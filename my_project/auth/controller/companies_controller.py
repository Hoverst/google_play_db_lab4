from flask import request, jsonify, abort
from my_project.auth.dto import companies_dto
from my_project.auth.service import companies_service


def get_all():
    return jsonify(companies_service.get_all()), 200


def get_by_id(company_id):
    return jsonify(companies_service.get_by_id(company_id)), 200


def create():
    data = companies_dto.parse_create(request.get_json(silent=True))
    return jsonify(companies_service.create(data)), 201


def update(company_id):
    data = companies_dto.parse_put(request.get_json(silent=True))
    return jsonify(companies_service.update(company_id, data, partial=False)), 200


def patch(company_id):
    data = companies_dto.parse_patch(request.get_json(silent=True))
    return jsonify(companies_service.update(company_id, data, partial=True)), 200


def delete(company_id):
    companies_service.delete(company_id)
    return "", 204


def get_apps(company_id):
    from my_project.auth.dao import companies_dao
    company = companies_dao.find_by_id(company_id)
    if company is None:
        abort(404)
    return jsonify([a.to_dict() for a in company.apps]), 200
