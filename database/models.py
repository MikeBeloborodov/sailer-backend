from database_logic import Base
from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.sql.sqltypes import TIMESTAMP
from sqlalchemy.sql.expression import text


class User(Base):
    __tablename__ = "users"

    user_id = Column(Integer, primary_key=True, nullable=False)
    email = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False)
    created_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('now()'))
    updated_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('now()'))
    phone = Column(String, unique=True, nullable=False)
    name = Column(String, nullable=False)
    user_credits = Column(Float, nullable=False, server_default=text(0))
    avatar = Column(String, nullable=False, server_default=text('https://cdn.pixabay.com/photo/2018/11/13/21/43/avatar-3814049__480.png'))
