from flask import request, jsonify
from sqlalchemy.exc import IntegrityError
from my_project import db
from my_project.auth.service import bills_service

def get_all():
    result = bills_service.get_all()
    return jsonify(result), 200

def get_by_id(account_id, app_id):
    result = bills_service.get_by_id(account_id, app_id)
    return jsonify(result), 200

def create():
    data = request.get_json(silent=True)
    if data is None:
        return jsonify({"error": "No input data provided"}), 400
    try:
        result = bills_service.create(data)
        return jsonify(result), 201
    except IntegrityError as e:
        db.session.rollback()
        return jsonify({"error": "Integrity constraint violated: " + str(e.orig)}), 409

def update(account_id, app_id):
    data = request.get_json(silent=True)
    if data is None:
        return jsonify({"error": "No input data provided"}), 400
    try:
        result = bills_service.update(account_id, app_id, data, partial=False)
        return jsonify(result), 200
    except IntegrityError as e:
        db.session.rollback()
        return jsonify({"error": "Integrity constraint violated: " + str(e.orig)}), 409

def patch(account_id, app_id):
    data = request.get_json(silent=True)
    if data is None:
        return jsonify({"error": "No input data provided"}), 400
    try:
        result = bills_service.update(account_id, app_id, data, partial=True)
        return jsonify(result), 200
    except IntegrityError as e:
        db.session.rollback()
        return jsonify({"error": "Integrity constraint violated: " + str(e.orig)}), 409

def delete(account_id, app_id):
    try:
        bills_service.delete(account_id, app_id)
        return "", 204
    except IntegrityError as e:
        db.session.rollback()
        return jsonify({"error": "Integrity constraint violated: " + str(e.orig)}), 409
