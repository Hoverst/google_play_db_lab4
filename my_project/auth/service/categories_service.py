from flask import abort
from sqlalchemy.exc import IntegrityError
from my_project.auth.dao import categories_dao


def get_all():
    return [c.to_dict() for c in categories_dao.find_all()]


def get_by_id(category_id):
    category = categories_dao.find_by_id(category_id)
    if category is None:
        abort(404)
    return category.to_dict()


def create(data):
    try:
        category = categories_dao.create(data)
    except IntegrityError:
        abort(409, description="Category name already exists")
    return category.to_dict()


def update(category_id, data, partial=False):
    category = categories_dao.find_by_id(category_id)
    if category is None:
        abort(404)
    try:
        category = categories_dao.update(category, data)
    except IntegrityError:
        abort(409, description="Category name already exists")
    return category.to_dict()


def delete(category_id):
    category = categories_dao.find_by_id(category_id)
    if category is None:
        abort(404)
    if category.apps:
        abort(409, description="Cannot delete category linked to apps")
    try:
        categories_dao.delete(category)
    except IntegrityError:
        abort(409, description="Cannot delete category due to related records")
