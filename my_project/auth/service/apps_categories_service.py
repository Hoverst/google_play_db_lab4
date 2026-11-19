from flask import abort
from sqlalchemy.exc import IntegrityError
from my_project.auth.dao import apps_dao, categories_dao, apps_categories_dao


def list_categories(app_id):
    app = apps_dao.find_by_id(app_id)
    if app is None:
        abort(404)
    return [c.to_dict() for c in app.categories]


def list_apps(category_id):
    category = categories_dao.find_by_id(category_id)
    if category is None:
        abort(404)
    return [a.to_dict() for a in category.apps]


def attach(app_id, category_id):
    app = apps_dao.find_by_id(app_id)
    if app is None:
        abort(404)
    category = categories_dao.find_by_id(category_id)
    if category is None:
        abort(404)
    if apps_categories_dao.find_link(app_id, category_id) is not None:
        abort(409, description="App already linked to this category")
    try:
        link = apps_categories_dao.create_link(app_id, category_id)
    except IntegrityError:
        abort(409, description="App already linked to this category")
    return link.to_dict()


def detach(app_id, category_id):
    app = apps_dao.find_by_id(app_id)
    if app is None:
        abort(404)
    link = apps_categories_dao.find_link(app_id, category_id)
    if link is None:
        abort(404)
    apps_categories_dao.delete_link(link)
