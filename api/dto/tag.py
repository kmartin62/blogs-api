from dataclasses import dataclass

@dataclass
class TagDto:
  id: int
  name: str
  description: str