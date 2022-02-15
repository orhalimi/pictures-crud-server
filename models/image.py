from models.base import Base
from sqlalchemy import Column, Integer, String, ForeignKey


class Image(Base):
    __tablename__ = 'images'
    id = Column(Integer(), primary_key=True, unique=True, autoincrement=True)
    owner_id = Column(Integer(), ForeignKey(
        'user.id', ondelete="CASCADE", onupdate="RESTRICT"), nullable=False)
    image_id = Column(Integer(), ForeignKey(
        'images.id', ondelete="CASCADE", onupdate="RESTRICT"), nullable=False)
    tag = Column(String(120))

    def __repr__(self):
        return f"Image id={self.id} owner_id={self.owner_id} image_blob={self.image_blob} create_date={self.create_date}"
