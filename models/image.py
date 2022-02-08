import base
from sqlalchemy import Column, Integer, String, BLOB, DateTime
from datetime import datetime


class Image(base.Base):
    __tablename__ = 'images'
    id = Column(Integer(), primary_key=True, unique=True, autoincrement=True)
    owner = Column(String(80))
    image_blob = Column(BLOB(), nullable=False)
    create_date = Column(DateTime(), default=datetime.utcnow())

    def __repr__(self):
        return f"Image id={self.id} owner={self.owner} image_blob={self.image_blob} create_date={self.create_date}"
