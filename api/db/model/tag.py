from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from db.db_config import Base

class Tag(Base):
  __tablename__ = "tag"
  id = Column(Integer, primary_key=True)
  name = Column(String(100), nullable=False)
  description = Column(String(100), nullable=True)

  posts = relationship("Post", secondary="posttags", back_populates="tags")