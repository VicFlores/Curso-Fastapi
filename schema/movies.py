from typing import Optional
from pydantic import BaseModel, Field


class Movie(BaseModel):
    id: Optional[int] = None
    title: str = Field(min_length=4, max_length=15)
    overview: str = Field(min_length=4, max_length=200)
    year: int = Field(ge=1900, le=2030)
    rating: float = Field(ge=0.0, le=10.0)
    category: str = Field(min_length=4, max_length=15)

    class Config:
        schema_extra = {
            "example": {
                "id": 1,
                "title": "The Shawshank Redemption",
                "overview": "Two imprisoned",
                "year": 1994,
                "rating": 9.3,
                "category": "Drama"
            }
        }
