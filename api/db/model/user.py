from sqlalchemy import Column, DateTime, Integer, String, UniqueConstraint
from datetime import datetime
from db.db_config import Base

class User(Base):
  __tablename__ = "users"
  id = Column(Integer, primary_key=True)
  first_name = Column(String(100), nullable=False)
  last_name = Column(String(100), nullable=False)
  email = Column(String(100), nullable=False)
  password = Column(String, nullable=False)
  middle_name = Column(String(100), nullable=True)
  created_at = Column(DateTime, default=datetime.now())
  updated_at = Column(DateTime, nullable=True, default=None)

  __table_args__ = (UniqueConstraint("email"),)