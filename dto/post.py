from dataclasses import dataclass
from datetime import datetime
from typing import List

from dto.category import Category
from dto.tag import Tag

@dataclass
class Post:
  title: str
  content: str
  published: bool
  category: Category
  tags: List[Tag]
  published_at: datetime
  updated_at: datetime
