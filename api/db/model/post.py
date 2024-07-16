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
    category_id = Column(Integer, ForeignKey('category.id'), nullable=False)

    tags = relationship("Tag", secondary="posttags", back_populates="posts", lazy='joined')
    category = relationship("Category", back_populates="posts", lazy='joined')

    def to_dict(self):
        return {"id": self.id,
                "title": self.title,
                "content": self.content,
                "created_by": self.created_by,
                "published_at": self.published_at,
                "updated_at": self.updated_at,
                "category": {
                    "id": self.category.id,
                    "title": self.category.title,
                    "description": self.category.description
                }, "tags": [
                    {
                        "id": tag.id,
                        "name": tag.name,
                        "description": tag.description
                    } for tag in self.tags
                ]}
  