from my_project import db

class AccountDevice(db.Model):

    __tablename__ = 'accounts_devices'
    __table_args__ = (
        db.PrimaryKeyConstraint('account_id', 'device_id'),
    )

    account_id = db.Column(db.Integer, db.ForeignKey('accounts.id'), nullable=False)
    device_id = db.Column(db.Integer, db.ForeignKey('devices.id'), nullable=False)

    account = db.relationship('Account', lazy='select', overlaps='accounts,devices')
    device = db.relationship('Device', lazy='select', overlaps='accounts,devices')

    def to_dict(self):
        return {
            'account_id': self.account_id,
            'device_id': self.device_id
        }
