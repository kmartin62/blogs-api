from abc import ABC
from dataclasses import dataclass

@dataclass
class DatabaseEnvironment(ABC):
    user: str = 'blog_admin'
    password: str = 'DQZ7iH10v8hH7Wn'
    host: str = 'localhost'
    port: int = 5432
    database: str = 'blogs'