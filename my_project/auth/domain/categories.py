from my_project import db

class Category(db.Model):

    __tablename__ = 'categories'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(45), nullable=False, unique=True)

    apps = db.relationship('App', secondary='apps_categories', back_populates='categories', lazy='select')

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name
        }
