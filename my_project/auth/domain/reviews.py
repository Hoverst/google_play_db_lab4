from my_project import db
from sqlalchemy.dialects.mysql import INTEGER


class Review(db.Model):
    __tablename__ = "reviews"
    __table_args__ = (
        db.UniqueConstraint("account_id", "app_id", name="uq_reviews_account_id_app_id"),
        db.ForeignKeyConstraint(
            ["account_id", "app_id"],
            ["library.account_id", "library.app_id"],
            name="fk_reviews_library",
            ondelete="RESTRICT",
            onupdate="RESTRICT",
        ),
        db.CheckConstraint("rating BETWEEN 0.0 AND 5.0", name="chk_reviews_rating"),
    )

    id = db.Column(INTEGER(unsigned=True), primary_key=True, autoincrement=True)
    account_id = db.Column(INTEGER(unsigned=True), nullable=False)
    app_id = db.Column(INTEGER(unsigned=True), nullable=False)
    rating = db.Column(db.Numeric(2, 1), nullable=False)
    comment = db.Column(db.String(350), nullable=True)
    created_at = db.Column(db.DateTime, nullable=False, server_default=db.func.current_timestamp())
    updated_at = db.Column(db.DateTime, nullable=True)

    app = db.relationship(
        "App",
        primaryjoin="foreign(Review.app_id)==App.id",
        viewonly=True,
        lazy="select",
    )

    def to_dict(self):
        return {
            "id": self.id,
            "account_id": self.account_id,
            "app_id": self.app_id,
            "rating": float(self.rating) if self.rating is not None else None,
            "comment": self.comment,
            "created_at": self.created_at.isoformat() if self.created_at else None,
            "updated_at": self.updated_at.isoformat() if self.updated_at else None,
        }
