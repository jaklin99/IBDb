from sqlalchemy.orm import relationship

from app.database import Base
import sqlalchemy as sa

class Review(Base):
<<<<<<< HEAD
    __tablename__ = "Reviews"
=======
    __tablename__ = "Review"
>>>>>>> 65c530dc3ff53bccb3ee14a8f4b31d4238c52a47
    id = sa.Column(sa.Integer, primary_key=True, autoincrement=True)
    content = sa.Column(sa.String(length=255), nullable=False)
    # book = sa.Column(sa.String(length=255), nullable=False)
    # user = sa.Column(sa.String(length=255), nullable=False)
<<<<<<< HEAD
    date = sa.Column(sa.DATE, nullable=False)

    # user_id = sa.Column(sa.Integer, foregn_key="users.id")
    # user = relationship("User", back_populates="books") and books must be created as a relationship in User
=======
    date = sa.Column(sa.DATETIME, nullable=False)

    # user_id = sa.Column(sa.Integer, foregn_key="users.id")
    # user = relationship("User", back_populates="books") and books must be created as a relationship in User
>>>>>>> 65c530dc3ff53bccb3ee14a8f4b31d4238c52a47
