"""Controller for payment_cards CRUD operations and relationship endpoints."""

from flask import request, jsonify, abort
from sqlalchemy.exc import IntegrityError
from my_project import db
from my_project.auth.domain.payment_cards import PaymentCard
from my_project.auth.service import payment_cards_service


def get_all():
    """Return all payment cards."""
    result = payment_cards_service.get_all()
    return jsonify(result), 200


def get_by_id(card_id):
    """Return a single payment card by ID."""
    result = payment_cards_service.get_by_id(card_id)
    return jsonify(result), 200


def create():
    """Create a new payment card."""
    data = request.get_json()
    if not data:
        return jsonify({"error": "No input data provided"}), 400
    try:
        result = payment_cards_service.create(data)
        return jsonify(result), 201
    except IntegrityError as e:
        db.session.rollback()
        return jsonify({"error": "Integrity constraint violated: " + str(e.orig)}), 409


def update(card_id):
    """Update an existing payment card."""
    data = request.get_json()
    if not data:
        return jsonify({"error": "No input data provided"}), 400
    try:
        result = payment_cards_service.update(card_id, data)
        return jsonify(result), 200
    except IntegrityError as e:
        db.session.rollback()
        return jsonify({"error": "Integrity constraint violated: " + str(e.orig)}), 409


def delete(card_id):
    """Delete a payment card by ID."""
    try:
        payment_cards_service.delete(card_id)
        return "", 204
    except IntegrityError as e:
        db.session.rollback()
        return jsonify({"error": "Integrity constraint violated: " + str(e.orig)}), 409


# --- Relationship endpoints ---

def get_bills(card_id):
    """Return all bills paid with a given payment card."""
    card = PaymentCard.query.get(card_id)
    if card is None:
        abort(404)
    return jsonify([item.to_dict() for item in card.bills]), 200
