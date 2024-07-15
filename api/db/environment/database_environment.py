from abc import ABC
from dataclasses import dataclass

@dataclass
class DatabaseEnvironment(ABC):
    user: str = 'myuser'
    password: str = 'mysecretpassword'
    host: str = 'localhost'
    port: int = 5432
    database: str = 'mydatabase'