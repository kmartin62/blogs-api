from dataclasses import dataclass

@dataclass
class CategoryDto:
  id: int
  title: str
  description: str