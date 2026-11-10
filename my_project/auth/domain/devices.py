from my_project import db

class Device(db.Model):

    __tablename__ = 'devices'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    model = db.Column(db.String(45), nullable=False)
    os_version = db.Column(db.String(20), nullable=False)

    accounts = db.relationship('Account', secondary='accounts_devices', back_populates='devices', lazy='select')
    installations = db.relationship('Installation', back_populates='device', lazy='select')

    def to_dict(self):
        return {
            'id': self.id,
            'model': self.model,
            'os_version': self.os_version
        }
