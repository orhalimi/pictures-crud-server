import base
from sqlalchemy import Column, Integer, String, ForeignKey
from datetime import datetime


class ImageTag(base.Base):
    __tablename__ = 'images_tags'
    id = Column(Integer(), primary_key=True, unique=True, autoincrement=True)
    image_id = Column(Integer(), ForeignKey('images.id', ondelete="CASCADE", onupdate="RESTRICT"), nullable=False)
    tag = Column(String(120))


    def __repr__(self):
        return f"Image id={self.id} owner={self.owner} image_blob={self.image_blob} create_date={self.create_date}"
