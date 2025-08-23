from __future__ import annotations
from pydantic import BaseModel, ConfigDict
from typing import Optional, List



class Blog(BaseModel):
    title: str
    body: str
    user_id: int

class User(BaseModel):
    name: str
    email: str
    password: str

# ----- OUTPUT DTOs (fără recursie) -----
class ShowUserBrief(BaseModel):
    id: int
    name: str
    email: str
    model_config = ConfigDict(from_attributes=True)

class ShowBlogBrief(BaseModel):
    id: int
    title: str
    body: str
    model_config = ConfigDict(from_attributes=True)

class ShowBlog(ShowBlogBrief):
    # când returnăm un blog, arătăm autorul într-o formă „brief”
    creator: Optional[ShowUserBrief] = None
    model_config = ConfigDict(from_attributes=True)

class ShowUser(ShowUserBrief):
    # când returnăm un user, arătăm lista de bloguri fără câmpul creator
    blogs: List[ShowBlogBrief] = []
    model_config = ConfigDict(from_attributes=True)


class Login(BaseModel):
    username: str
    password: str 

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    email: Optional[str] = None
    

    
ShowUser.model_rebuild()
ShowBlog.model_rebuild()