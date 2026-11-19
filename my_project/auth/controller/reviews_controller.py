from flask import request, jsonify, abort
from my_project.auth.dto import reviews_dto
from my_project.auth.service import reviews_service


def get_all():
    return jsonify(reviews_service.get_all()), 200


def get_by_id(review_id):
    return jsonify(reviews_service.get_by_id(review_id)), 200


def create():
    data = reviews_dto.parse_create(request.get_json(silent=True))
    return jsonify(reviews_service.create(data)), 201


def update(review_id):
    data = reviews_dto.parse_put(request.get_json(silent=True))
    return jsonify(reviews_service.update(review_id, data, partial=False)), 200


def patch(review_id):
    data = reviews_dto.parse_patch(request.get_json(silent=True))
    return jsonify(reviews_service.update(review_id, data, partial=True)), 200


def delete(review_id):
    reviews_service.delete(review_id)
    return "", 204
