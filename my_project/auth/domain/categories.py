# categories.py - SQLAlchemy model for the 'categories' table

from my_project import db


class Category(db.Model):
    """Represents an app category in the play_store database."""

    __tablename__ = 'categories'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(45), nullable=False, unique=True)

    # Relationships
    apps = db.relationship('App', secondary='apps_categories', back_populates='categories', lazy='select')

    def to_dict(self):
        """Convert all columns to a JSON-safe dictionary."""
        return {
            'id': self.id,
            'name': self.name
        }
