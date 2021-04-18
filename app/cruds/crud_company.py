from typing import List

from sqlalchemy.orm import Session

from app.crud.base import CRUDBase
from app.models.company import Company
from app.schemas.company import CompanyCreate, CompanyUpdate

class CRUDCompany(CRUDBase[Company, CompanyCreate, CompanyUpdate]):
    def get_by_ids(
        self,
        db: Session,
        *,
        company_ids: List[int]
    ) -> List[Company]:
        return db.query(Company).filter(Company.id.in_(company_ids)).all()


company = CRUDCompany(Company)