from sqlalchemy.orm import relationship

from app.database import Base
import sqlalchemy as sa

class Review(Base):
    __tablename__ = "Review"
    id = sa.Column(sa.Integer, primary_key=True, autoincrement=True)
    content = sa.Column(sa.String(length=255), nullable=False)
    book = sa.Column(sa.String(length=255), nullable=False)
    user = sa.Column(sa.String(length=255), nullable=False)
    datetime = sa.Column(sa.DATETIME, nullable=False)

    # user_id = sa.Column(sa.Integer, foregn_key="users.id")
    # user = relationship("User", back_populates="books") and books must be created as a relationship in User