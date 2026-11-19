from my_project import db
from sqlalchemy.dialects.mysql import INTEGER, BIGINT


class AppVersion(db.Model):
    __tablename__ = "apps_versions"
    __table_args__ = (
        db.UniqueConstraint("app_id", "version", name="uq_apps_versions_app_id_version"),
    )

    id = db.Column(INTEGER(unsigned=True), primary_key=True, autoincrement=True)
    app_id = db.Column(
        INTEGER(unsigned=True), db.ForeignKey("apps.id", ondelete="RESTRICT"), nullable=False
    )
    version = db.Column(db.String(20), nullable=False)
    size_bytes = db.Column(BIGINT(unsigned=True), nullable=False)
    created_at = db.Column(db.DateTime, nullable=False, server_default=db.func.current_timestamp())

    app = db.relationship("App", back_populates="versions", lazy="select")
    installations = db.relationship("Installation", back_populates="app_version", lazy="select")

    def to_dict(self):
        return {
            "id": self.id,
            "app_id": self.app_id,
            "version": self.version,
            "size_bytes": self.size_bytes,
            "created_at": self.created_at.isoformat() if self.created_at else None,
        }
