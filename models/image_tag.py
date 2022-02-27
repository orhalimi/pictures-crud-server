from models.base import Base
from sqlalchemy import Column, Integer, String, ForeignKey
from datetime import datetime
from utils.decorators import sqlalchemy_repr


@sqlalchemy_repr
class ImageTag(Base):
    __tablename__ = 'images_tags'
    id = Column(Integer(), primary_key=True, unique=True, autoincrement=True)
    image_id = Column(Integer(), ForeignKey(
        'images.id', ondelete="CASCADE", onupdate="RESTRICT"), nullable=False)
    tag = Column(String(120))

    def __repr__(self):
        return f"Image id={self.id} image_id={self.image_id} tag={self.tag}"
