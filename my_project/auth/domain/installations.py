from my_project import db
from sqlalchemy.dialects.mysql import INTEGER


class Installation(db.Model):
    __tablename__ = "installations"
    __table_args__ = (
        db.UniqueConstraint(
            "device_id", "app_version_id", name="uq_installations_device_id_app_version_id"
        ),
    )

    id = db.Column(INTEGER(unsigned=True), primary_key=True, autoincrement=True)
    device_id = db.Column(
        INTEGER(unsigned=True), db.ForeignKey("devices.id", ondelete="CASCADE"), nullable=False
    )
    app_version_id = db.Column(
        INTEGER(unsigned=True),
        db.ForeignKey("apps_versions.id", ondelete="RESTRICT"),
        nullable=False,
    )
    installed_at = db.Column(db.DateTime, nullable=False, server_default=db.func.current_timestamp())
    updated_at = db.Column(db.DateTime, nullable=True)

    device = db.relationship("Device", back_populates="installations", lazy="select")
    app_version = db.relationship("AppVersion", back_populates="installations", lazy="select")

    def to_dict(self):
        return {
            "id": self.id,
            "device_id": self.device_id,
            "app_version_id": self.app_version_id,
            "installed_at": self.installed_at.isoformat() if self.installed_at else None,
            "updated_at": self.updated_at.isoformat() if self.updated_at else None,
        }
