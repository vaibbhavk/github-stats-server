from pydantic import BaseModel

from typing import Optional

class User(BaseModel):
    login: str
    id: int
    avatar_url: str
    html_url: str
    name: Optional[str]
    location: Optional[str]
    bio: Optional[str]
    twitter_username: Optional[str]