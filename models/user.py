from models.base import Base
from sqlalchemy import Column, Integer, String, ForeignKey


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer(), primary_key=True, unique=True, autoincrement=True, nullable=False)
    username = Column(String(21), nullable=False)
    password = Column(String(32), nullable=False)
    salt = Column(String(8), nullable=False)

    def __repr__(self):
        return f"User id={self.id} username={self.username} password={self.password} salt={self.salt}"
