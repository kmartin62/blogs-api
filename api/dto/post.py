from dataclasses import dataclass
from datetime import datetime
from typing import List

from dto.category import CategoryDto
from dto.tag import TagDto

@dataclass
class PostDto:
  title: str
  content: str
  category: CategoryDto
  tags: List[TagDto]