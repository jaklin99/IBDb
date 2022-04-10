from sqlalchemy.orm import relationship

from app.database.database import Base
import sqlalchemy as sa

class Book(Base):
    __tablename__ = "Books"
    id = sa.Column(sa.Integer, primary_key=True, autoincrement=True)
    title = sa.Column(sa.String(length=255), nullable=False)
    # author = sa.Column(sa.String(length=255), nullable=False)
    # genre = sa.Column(sa.String(length=255), nullable=False)
    # year = sa.Column(sa.Integer, nullable=False)
    # user_id = sa.Column(sa.Integer, foregn_key="users.id")
    # user = relationship("User", back_populates="books") #and books must be created as a relationship in User

