from sqlalchemy import Column, DateTime, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from datetime import datetime

from db.db_config import Base

class Post(Base):
    __tablename__ = "post"
    id = Column(Integer, primary_key=True)
    title = Column(String(100), nullable=False)
    content = Column(String(100), nullable=False)
    created_by = Column(String(100), ForeignKey('users.email'), nullable=False)
    published_at = Column(DateTime, default=datetime.now)
    updated_at = Column(DateTime, nullable=True, default=None)

    tags = relationship("Tag", secondary="posttags", back_populates="posts")
    category = relationship("Category", secondary="postcategory", back_populates="posts")
  