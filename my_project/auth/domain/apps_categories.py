from my_project import db

class AppCategory(db.Model):

    __tablename__ = 'apps_categories'
    __table_args__ = (
        db.PrimaryKeyConstraint('app_id', 'category_id'),
    )

    app_id = db.Column(db.Integer, db.ForeignKey('apps.id'), nullable=False)
    category_id = db.Column(db.Integer, db.ForeignKey('categories.id'), nullable=False)

    app = db.relationship('App', lazy='select', overlaps='apps,categories')
    category = db.relationship('Category', lazy='select', overlaps='apps,categories')

    def to_dict(self):
        return {
            'app_id': self.app_id,
            'category_id': self.category_id
        }
