from pydantic import BaseModel
from typing import Optional,List

class ChatRequest(BaseModel):
    query: str

class ChatResponse(BaseModel):
    answer: Optional[str] = None
    error: Optional[str] = None
    details: Optional[dict] = None

class UserContext(BaseModel):
    sub: str
    scope: Optional[str] = None