from models.base import Base
from sqlalchemy import Column, DATETIME, BLOB, Integer, String
from sqlalchemy.sql import func
from utils.decorators import sqlalchemy_repr


@sqlalchemy_repr
class Image(Base):
    __tablename__ = 'images'
    id = Column(Integer(), primary_key=True, unique=True, autoincrement=True)
    owner_id = Column(String(60), nullable=False)
    image_blob = Column(BLOB())
    create_date = Column(DATETIME(), nullable=False, default=func.now())
    name = Column(String(44))

