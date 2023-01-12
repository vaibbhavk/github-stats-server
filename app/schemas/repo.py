from pydantic import BaseModel

from typing import List, Optional

class Repo(BaseModel):
    id: int
    name: str
    html_url: str
    description: Optional[str]
    topics: List[str]
