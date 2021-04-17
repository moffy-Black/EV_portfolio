from database import Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from sqlalchemy_utils import UUIDType
from uuid import uuid4
from .mixins import TimestampMixin #add created_at & updated_at columns
from .like import like

class User(Base, TimestampMixin):
    __tablename__ = 'users'

    uuid = Column(UUIDType(binary=False),
    primary_key = True,
    default = uuid4)

    username = Column(String(128), nullable=False)

    companies = relationship(
        'Company',
        secondary=like,
        back_populates='users'
    )