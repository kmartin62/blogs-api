from .database_environment import DatabaseEnvironment

class PostgresEnvironment(DatabaseEnvironment):
  def __init__(self):
    pass

  def __repr__(self) -> str:
    return f'postgresql://{self.user}:{self.password}@{self.host}:{self.port}/{self.database}'