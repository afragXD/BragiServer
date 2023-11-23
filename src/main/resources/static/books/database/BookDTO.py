from dataclasses import dataclass

@dataclass
class BookDTO:
    name: str
    en_name: str
    image: str
    description: str
    rating: float
    status: str
    chapters: int
    year: int
    author: str