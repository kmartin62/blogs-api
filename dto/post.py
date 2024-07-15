from dataclasses import dataclass
from datetime import datetime
from typing import List

from dto.tag import Tag

@dataclass
class Post:
  title: str
  content: str
  published: bool
  category_id: int
  tags: List[Tag]
  published_at: datetime
  updated_at: datetime
