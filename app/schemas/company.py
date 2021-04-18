from pydantic import BaseModel
from typing import Optional
from uuid import UUID

class CompanyBase(BaseModel):
    companyname: Optional[str] = None
    local: Optional[str] = None

class CompanyCreate(CompanyBase):
    companyname: str
    local: str

class CompanyUpdate(CompanyBase):
    pass

class CompanyInDBBase(CompanyBase):
    uuid: UUID

    class Config:
        orm_mode = True

class Company(CompanyInDBBase):
    pass

class CompanyInDB(CompanyInDBBase):
    pass