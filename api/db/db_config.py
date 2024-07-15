from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker
import logging
from .db_factory import DatabaseFactory
from sqlalchemy.exc import ArgumentError, OperationalError

class DatabaseConfiguration:
  def __init__(self, database_uri):
    self.DATABASE_URI = database_uri
    self.engine = create_engine(self.DATABASE_URI)
    try:
      self.engine.connect()
      self.base = declarative_base()
      self.session = sessionmaker(bind=self.engine)
    except ArgumentError as argument_err:
      logging.error(f"An ArgumentError occured. Error message: {repr(argument_err)}")
      self.base = None
      self.session = None
    except OperationalError as operational_err:
      logging.error(f"An OperationalError occured. Error message: {repr(operational_err)}")
      self.base = None
      self.session = None
    except Exception as ex:
      logging.error(f"An Exception occured. Error message: {repr(ex)}")
      self.base = None
      self.session = None

configuration = DatabaseConfiguration(database_uri=DatabaseFactory.get_database_connection_string("postgres"))

Base = configuration.base
Session = configuration.session