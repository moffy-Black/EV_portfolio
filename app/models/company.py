from database import Base
from sqlalchemy import Column, ForeignKey, String
from sqlalchemy.orm import relationship
from sqlalchemy_utils import UUIDType
from uuid import uuid4
from .mixins import TimestampMixin
from .like import like

class Company(Base, TimestampMixin):
    __tablename__ = 'companies'

    uuid = Column(UUIDType(binary=False),
    primary_key=True,
    default=uuid4)

    companyname = Column(String(256), nullable=False),

    users = relationship(
        "User",
        secondary=like,
        back_populates="companies"
    )