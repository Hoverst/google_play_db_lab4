# apps_categories.py - SQLAlchemy model for the 'apps_categories' junction table

from my_project import db


class AppCategory(db.Model):
    """Junction table linking apps and categories."""

    __tablename__ = 'apps_categories'
    __table_args__ = (
        db.PrimaryKeyConstraint('app_id', 'category_id'),
    )

    app_id = db.Column(db.Integer, db.ForeignKey('apps.id'), nullable=False)
    category_id = db.Column(db.Integer, db.ForeignKey('categories.id'), nullable=False)

    # Relationships (overlaps silences secondary= conflicts with App.categories / Category.apps)
    app = db.relationship('App', lazy='select', overlaps='apps,categories')
    category = db.relationship('Category', lazy='select', overlaps='apps,categories')

    def to_dict(self):
        """Convert all columns to a JSON-safe dictionary."""
        return {
            'app_id': self.app_id,
            'category_id': self.category_id
        }
