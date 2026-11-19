from flask import abort
from sqlalchemy.exc import IntegrityError
from my_project.auth.dao import apps_dao, companies_dao
from my_project.auth.domain.apps import AppStatus


def get_all():
    return [a.to_dict() for a in apps_dao.find_all()]


def get_by_id(app_id):
    app = apps_dao.find_by_id(app_id)
    if app is None:
        abort(404)
    return app.to_dict()


def create(data):
    if companies_dao.find_by_id(data["company_id"]) is None:
        abort(400, description="company_id must reference an existing company")
    try:
        app = apps_dao.create(data)
    except IntegrityError:
        abort(409, description="package_name already exists")
    return app.to_dict()


def update(app_id, data, partial=False):
    app = apps_dao.find_by_id(app_id)
    if app is None:
        abort(404)
    if "company_id" in data and companies_dao.find_by_id(data["company_id"]) is None:
        abort(400, description="company_id must reference an existing company")
    try:
        app = apps_dao.update(app, data)
    except IntegrityError:
        abort(409, description="package_name already exists")
    return app.to_dict()


def delete(app_id):
    """DELETE /apps/<id>.

    - no dependents      -> hard delete, returns None (controller answers 204)
    - has dependents      -> soft delete via status='unpublished', returns the app dict (200)
    - suspended apps keep 'suspended' (never downgraded) but are still returned with 200.
    """
    app = apps_dao.find_by_id(app_id)
    if app is None:
        abort(404)
    if apps_dao.has_dependents(app_id):
        return _soft_delete(app)
    try:
        apps_dao.delete(app)
        return None
    except IntegrityError:
        # A dependent row appeared between the check and the delete: fall back to soft delete.
        app = apps_dao.find_by_id(app_id)
        if app is None:
            abort(409, description="Cannot delete app due to related records")
        return _soft_delete(app)


def _soft_delete(app):
    if app.status != AppStatus.suspended:
        app = apps_dao.update(app, {"status": AppStatus.unpublished})
    return app.to_dict()


def get_versions(app_id):
    app = apps_dao.find_by_id(app_id)
    if app is None:
        abort(404)
    return [v.to_dict() for v in app.versions]


def get_reviews(app_id):
    app = apps_dao.find_by_id(app_id)
    if app is None:
        abort(404)
    return [r.to_dict() for r in app.reviews]


def get_library(app_id):
    app = apps_dao.find_by_id(app_id)
    if app is None:
        abort(404)
    return [e.to_dict() for e in app.library_entries]
