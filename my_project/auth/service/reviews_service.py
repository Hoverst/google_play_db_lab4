from datetime import datetime, timezone
from flask import abort
from sqlalchemy.exc import IntegrityError
from my_project.auth.dao import reviews_dao, library_dao, accounts_dao


def get_all():
    return [r.to_dict() for r in reviews_dao.find_all()]


def get_by_id(review_id):
    review = reviews_dao.find_by_id(review_id)
    if review is None:
        abort(404)
    return review.to_dict()


def create(data):
    if accounts_dao.find_by_id_active(data["account_id"]) is None:
        abort(400, description="account_id must reference an existing non-deleted account")
    lib = library_dao.find_by_account_and_app(data["account_id"], data["app_id"])
    if lib is None:
        abort(409, description="Review requires an existing library entry for this account and app")
    try:
        review = reviews_dao.create(data)
    except IntegrityError:
        abort(409, description="Review already exists for this account and app")
    return review.to_dict()


def update(review_id, data, partial=False):
    review = reviews_dao.find_by_id(review_id)
    if review is None:
        abort(404)
    payload = dict(data)
    payload["updated_at"] = datetime.now(timezone.utc).replace(tzinfo=None)
    try:
        review = reviews_dao.update(review, payload)
    except IntegrityError:
        abort(409, description="Conflict updating review")
    return review.to_dict()


def delete(review_id):
    review = reviews_dao.find_by_id(review_id)
    if review is None:
        abort(404)
    reviews_dao.delete(review)
