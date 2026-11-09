# accounts_devices.py - SQLAlchemy model for the 'accounts_devices' junction table

from my_project import db


class AccountDevice(db.Model):
    """Junction table linking accounts and devices."""

    __tablename__ = 'accounts_devices'
    __table_args__ = (
        db.PrimaryKeyConstraint('account_id', 'device_id'),
    )

    account_id = db.Column(db.Integer, db.ForeignKey('accounts.id'), nullable=False)
    device_id = db.Column(db.Integer, db.ForeignKey('devices.id'), nullable=False)

    # Relationships (overlaps silences secondary= conflicts with Account.devices / Device.accounts)
    account = db.relationship('Account', lazy='select', overlaps='accounts,devices')
    device = db.relationship('Device', lazy='select', overlaps='accounts,devices')

    def to_dict(self):
        """Convert all columns to a JSON-safe dictionary."""
        return {
            'account_id': self.account_id,
            'device_id': self.device_id
        }
