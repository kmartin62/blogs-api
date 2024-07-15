import unittest

from api.db.db_config import DatabaseConfiguration
from api.db.db_factory import DatabaseFactory
from api.db.environment.postgres_environment import PostgresEnvironment
from sqlalchemy.exc import ArgumentError

class TestPostgresConfiguration(unittest.TestCase):
  def test_postgres_connection_string(self):
    conn_string = str(PostgresEnvironment())
    self.assertIsNotNone(conn_string)
    self.assertIsInstance(conn_string, str)
    assert conn_string.startswith("postgresql://")

  def test_postgres_sqlalchemy_configuration(self):
    configuration = DatabaseConfiguration(database_uri=DatabaseFactory.get_database_connection_string("postgres"))
    base = configuration.base
    session = configuration.session
    self.assertIsNotNone(base)
    self.assertIsNotNone(session)

    with self.assertRaises(ArgumentError):
      configuration = DatabaseConfiguration(database_uri="fail")
      base = configuration.base
      session = configuration.session
      self.assertIsNone(base)
      self.assertIsNone(session)  