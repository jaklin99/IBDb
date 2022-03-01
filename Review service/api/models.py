from .database import Base
import sqlalchemy as sa


class Book(Base):
    __tablename__ = "Book"
    id = sa.Column(sa.Integer, primary_key=True, autoincrement=True)
    content = sa.Column(sa.String(length=255), nullable=False)