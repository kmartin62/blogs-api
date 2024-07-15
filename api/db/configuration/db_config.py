from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from db_factory import DatabaseFactory

class DatabaseConfiguration:
  def __init__(self):
    self.DATABASE_URI = DatabaseFactory.get_database_connection_string("postgres")
    self.engine = create_engine(self.DATABASE_URI)
    self.base = declarative_base()
    self.session = sessionmaker(bind=self.engine)

configuration = DatabaseConfiguration()

Base = configuration.base
Session = configuration.session

print(Base)
print(Session)