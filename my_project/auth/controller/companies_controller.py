"""Controller for companies CRUD operations and relationship endpoints."""

from flask import request, jsonify, abort
from sqlalchemy.exc import IntegrityError
from my_project import db
from my_project.auth.domain.companies import Company
from my_project.auth.service import companies_service


def get_all():
    """Return all companies."""
    result = companies_service.get_all()
    return jsonify(result), 200


def get_by_id(company_id):
    """Return a single company by ID."""
    result = companies_service.get_by_id(company_id)
    return jsonify(result), 200


def create():
    """Create a new company."""
    data = request.get_json()
    if not data:
        return jsonify({"error": "No input data provided"}), 400
    try:
        result = companies_service.create(data)
        return jsonify(result), 201
    except IntegrityError as e:
        db.session.rollback()
        return jsonify({"error": "Integrity constraint violated: " + str(e.orig)}), 409


def update(company_id):
    """Update an existing company."""
    data = request.get_json()
    if not data:
        return jsonify({"error": "No input data provided"}), 400
    try:
        result = companies_service.update(company_id, data)
        return jsonify(result), 200
    except IntegrityError as e:
        db.session.rollback()
        return jsonify({"error": "Integrity constraint violated: " + str(e.orig)}), 409


def delete(company_id):
    """Delete a company by ID."""
    try:
        companies_service.delete(company_id)
        return "", 204
    except IntegrityError as e:
        db.session.rollback()
        return jsonify({"error": "Integrity constraint violated: " + str(e.orig)}), 409


# --- Relationship endpoints ---

def get_apps(company_id):
    """Return all apps for a given company."""
    company = Company.query.get(company_id)
    if company is None:
        abort(404)
    return jsonify([item.to_dict() for item in company.apps]), 200
