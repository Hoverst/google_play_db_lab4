from my_project import db

class Installation(db.Model):

    __tablename__ = 'installations'
    __table_args__ = (
        db.PrimaryKeyConstraint('app_id', 'device_id'),
    )

    app_id = db.Column(db.Integer, db.ForeignKey('apps.id'), nullable=False)
    device_id = db.Column(db.Integer, db.ForeignKey('devices.id'), nullable=False)
    installed_at = db.Column(db.DateTime, nullable=False, server_default=db.func.now())

    app = db.relationship('App', back_populates='installations', lazy='select')
    device = db.relationship('Device', back_populates='installations', lazy='select')

    def to_dict(self):
        return {
            'app_id': self.app_id,
            'device_id': self.device_id,
            'installed_at': self.installed_at.isoformat() if self.installed_at else None
        }
