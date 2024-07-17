from abc import ABC
from dataclasses import dataclass
import os
@dataclass
class DatabaseEnvironment(ABC):
    user: str = os.getenv("POSTGRES_USER")
    password: str = os.getenv("POSTGRES_PASSWORD")
    host: str = os.getenv("POSTGRES_HOST")
    port: int = os.getenv("POSTGRES_PORT")
    database: str = os.getenv("POSTGRES_DB")