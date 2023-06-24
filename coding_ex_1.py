from pydantic import BaseModel  
from typing import Optional, List, Dict
from datetime import date
from database import cars

class Comment(BaseModel):
    author: str
    comment: str
    likes: int


class Post(BaseModel):
    author: str
    co_author: Optional[str]=None
    date: date
    title: str
    content: str
    id: int
    likes: List[str]
    comments: List[Comment]

