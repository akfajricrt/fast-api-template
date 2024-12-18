from pydantic import BaseModel

class UserBase(BaseModel):
    username: str

class PostBase(BaseModel):
    title: str
    content: str
    user_id: int

