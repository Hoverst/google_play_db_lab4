from flask import request, jsonify, abort
from sqlalchemy.exc import IntegrityError
from my_project import db
from my_project.auth.domain.apps_discounts import AppDiscount
from my_project.auth.service import apps_discounts_service

def get_all():
    result = apps_discounts_service.get_all()
    return jsonify(result), 200

def get_by_id(discount_id):
    result = apps_discounts_service.get_by_id(discount_id)
    return jsonify(result), 200

def create():
    data = request.get_json(silent=True)
    if data is None:
        return jsonify({"error": "No input data provided"}), 400
    try:
        result = apps_discounts_service.create(data)
        return jsonify(result), 201
    except IntegrityError as e:
        db.session.rollback()
        return jsonify({"error": "Integrity constraint violated: " + str(e.orig)}), 409

def update(discount_id):
    data = request.get_json(silent=True)
    if data is None:
        return jsonify({"error": "No input data provided"}), 400
    try:
        result = apps_discounts_service.update(discount_id, data, partial=False)
        return jsonify(result), 200
    except IntegrityError as e:
        db.session.rollback()
        return jsonify({"error": "Integrity constraint violated: " + str(e.orig)}), 409

def patch(discount_id):
    data = request.get_json(silent=True)
    if data is None:
        return jsonify({"error": "No input data provided"}), 400
    try:
        result = apps_discounts_service.update(discount_id, data, partial=True)
        return jsonify(result), 200
    except IntegrityError as e:
        db.session.rollback()
        return jsonify({"error": "Integrity constraint violated: " + str(e.orig)}), 409

def delete(discount_id):
    try:
        apps_discounts_service.delete(discount_id)
        return "", 204
    except IntegrityError as e:
        db.session.rollback()
        return jsonify({"error": "Integrity constraint violated: " + str(e.orig)}), 409

def get_bills(discount_id):
    discount = AppDiscount.query.get(discount_id)
    if discount is None:
        abort(404)
    return jsonify([item.to_dict() for item in discount.bills]), 200
