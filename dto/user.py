from dataclasses import dataclass
from datetime import datetime

@dataclass
class User:
  first_name: str
  middle_name: str
  last_name: str
  email: str
  password: str
  created_at: datetime
  updated_at: datetime