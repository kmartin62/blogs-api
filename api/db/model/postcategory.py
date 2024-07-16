# from sqlalchemy import Column, ForeignKey, Integer, UniqueConstraint

# from db.db_config import Base

# class PostCategory(Base):
#   __tablename__ = "postcategory"
#   id = Column(Integer, primary_key=True)
#   post_id = Column(Integer, ForeignKey('post.id'), nullable=False)
#   category_id = Column(Integer, ForeignKey('category.id'), nullable=False)

#   __table_args__ = (UniqueConstraint("post_id", "category_id"),)