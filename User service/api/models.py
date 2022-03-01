from .database import Base
import sqlalchemy as sa


class User(Base):
    __tablename__ = "User"
    id = sa.Column(sa.Integer, primary_key=True, autoincrement=True)
    name = sa.Column(sa.String(length=255), nullable=False)