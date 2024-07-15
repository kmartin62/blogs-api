from environment.database_environment import DatabaseEnvironment
from environment import PostgresEnvironment


class DatabaseFactory:
  def __init__(self):
    pass

  @staticmethod
  def get_database_connection_string(db_type: str) -> str:
    if db_type == 'postgres':
      return str(PostgresEnvironment())
    else:
      return None