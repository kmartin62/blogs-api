from sqlalchemy import Column, ForeignKey, Integer, UniqueConstraint

from db.db_config import Base

class PostTags(Base):
  __tablename__ = "posttags"
  id = Column(Integer, primary_key=True)
  post_id = Column(Integer, ForeignKey('post.id'), nullable=False)
  tag_id = Column(Integer, ForeignKey('tag.id'), nullable=False)

  __table_args__ = (UniqueConstraint("post_id", "tag_id"),)