from sqlalchemy import Table, ForeignKey, Column, Integer

from database import Base

like = Table(
    'like',
    Base.metadata,
    Column('company_id', Integer, ForeignKey('company.uuid')),
    Column('user_id', Integer, ForeignKey('user.uuid'))
)