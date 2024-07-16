from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from db.db_config import Base

class Category(Base):
  __tablename__ = "category"
  id = Column(Integer, primary_key=True)
  title = Column(String(100), nullable=False)
  description = Column(String(100), nullable=True)

  posts = relationship("Post", secondary="postcategory", back_populates="category")