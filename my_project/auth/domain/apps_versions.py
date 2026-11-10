from my_project import db

class AppVersion(db.Model):

    __tablename__ = 'apps_versions'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    app_id = db.Column(db.Integer, db.ForeignKey('apps.id'), nullable=False)
    version = db.Column(db.String(20), nullable=False)
    size_bytes = db.Column(db.BigInteger, nullable=False)
    created_at = db.Column(db.DateTime, nullable=False, server_default=db.func.now())

    app = db.relationship('App', back_populates='versions', lazy='select')

    def to_dict(self):
        return {
            'id': self.id,
            'app_id': self.app_id,
            'version': self.version,
            'size_bytes': self.size_bytes,
            'created_at': self.created_at.isoformat() if self.created_at else None
        }
