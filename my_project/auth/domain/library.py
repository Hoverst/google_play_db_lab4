from my_project import db
from sqlalchemy.dialects.mysql import INTEGER


class Library(db.Model):
    __tablename__ = "library"
    __table_args__ = (
        db.UniqueConstraint("account_id", "app_id", name="uq_library_account_id_app_id"),
    )

    id = db.Column(INTEGER(unsigned=True), primary_key=True, autoincrement=True)
    app_id = db.Column(
        INTEGER(unsigned=True), db.ForeignKey("apps.id", ondelete="RESTRICT"), nullable=False
    )
    account_id = db.Column(
        INTEGER(unsigned=True), db.ForeignKey("accounts.id", ondelete="RESTRICT"), nullable=False
    )
    last_opened_at = db.Column(db.DateTime, nullable=True)
    added_at = db.Column(db.DateTime, nullable=False, server_default=db.func.current_timestamp())
    data_ref = db.Column(db.String(255), nullable=True)

    account = db.relationship("Account", back_populates="library_entries", lazy="select")
    app = db.relationship("App", back_populates="library_entries", lazy="select")
    review = db.relationship(
        "Review",
        primaryjoin="and_(Library.account_id==Review.account_id, Library.app_id==Review.app_id)",
        foreign_keys="[Review.account_id, Review.app_id]",
        uselist=False,
        viewonly=True,
        lazy="select",
    )

    def to_dict(self):
        return {
            "id": self.id,
            "app_id": self.app_id,
            "account_id": self.account_id,
            "last_opened_at": self.last_opened_at.isoformat() if self.last_opened_at else None,
            "added_at": self.added_at.isoformat() if self.added_at else None,
            "data_ref": self.data_ref,
        }
