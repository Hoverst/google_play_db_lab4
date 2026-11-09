# devices.py - SQLAlchemy model for the 'devices' table

from my_project import db


class Device(db.Model):
    """Represents a device in the play_store database."""

    __tablename__ = 'devices'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    model = db.Column(db.String(45), nullable=False)
    os_version = db.Column(db.String(20), nullable=False)

    # Relationships
    accounts = db.relationship('Account', secondary='accounts_devices', back_populates='devices', lazy='select')
    installations = db.relationship('Installation', back_populates='device', lazy='select')

    def to_dict(self):
        """Convert all columns to a JSON-safe dictionary."""
        return {
            'id': self.id,
            'model': self.model,
            'os_version': self.os_version
        }
