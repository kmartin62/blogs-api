from dataclasses import dataclass
from datetime import datetime

@dataclass
class UserDto:
  first_name: str
  middle_name: str
  last_name: str
  email: str
  password: str


@dataclass
class UserSignIn:
  email: str
  password: str