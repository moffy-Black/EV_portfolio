from typing import Optional,List
from pydantic import BaseModel
from uuid import UUID
from .company import Company

class UserBase(BaseModel):
    username: Optional[str] = None

class UserCreate(UserBase):
    pass

class UserUpdate(UserBase):
    pass

class UserInDBBase(UserBase):
    uuid: UUID

    class Config:
        orm_mode = True

class User(UserInDBBase):
    companies: List[Company]

class UserInDB(UserInDBBase):
    pass

class UserDetail(User):
    companies: List[Company] = []