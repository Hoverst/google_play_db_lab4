from my_project import db
from my_project.auth.domain.companies import Company


def find_all():
    return Company.query.all()


def find_by_id(id):
    return db.session.get(Company, id)


def find_by_developer_id(developer_id, exclude_company_id=None):
    q = Company.query.filter_by(developer_id=developer_id)
    if exclude_company_id is not None:
        q = q.filter(Company.id != exclude_company_id)
    return q.first()


def create(data):
    instance = Company(**data)
    try:
        db.session.add(instance)
        db.session.commit()
        return instance
    except Exception:
        db.session.rollback()
        raise


def update(instance, data):
    try:
        for key, value in data.items():
            setattr(instance, key, value)
        db.session.commit()
        return instance
    except Exception:
        db.session.rollback()
        raise


def delete(instance):
    try:
        db.session.delete(instance)
        db.session.commit()
    except Exception:
        db.session.rollback()
        raise
