from database.database_logic import Base
from sqlalchemy import Column, Integer, String, Float, ForeignKey, Boolean
from sqlalchemy.sql.sqltypes import TIMESTAMP
from sqlalchemy.sql.expression import text


class Item(Base):
    __tablename__ = "items"

    item_id = Column(Integer, primary_key=True, nullable=False)
    created_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('now()'))
    updated_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('now()'))
    owner_id = Column(Integer, ForeignKey("users.user_id", ondelete="CASCADE"), nullable=False)
    title = Column(String, nullable=False)
    description = Column(String, nullable=True)
    cathegory = Column(String, nullable=False)
    address = Column(String, nullable=False)
    condition = Column(String, nullable=False)
    price = Column(Float, nullable=False)
    photo = Column(String, nullable=True)
    buyer_id = Column(Integer, ForeignKey("users.user_id", ondelete="CASCADE"), nullable=True)
    transaction_id = Column(Integer, nullable=True)
    sold_at = Column(TIMESTAMP(timezone=True), nullable=True)
    reserved = Column(Boolean, nullable=False, server_default=text('false'))
    sold = Column(Boolean, nullable=False, server_default=text('false'))


class User(Base):
    __tablename__ = "users"

    user_id = Column(Integer, primary_key=True, nullable=False)
    email = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False)
    created_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('now()'))
    updated_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('now()'))
    phone_number = Column(String, unique=True, nullable=False)
    name = Column(String, nullable=False)
    user_credits = Column(Float, nullable=False, server_default=text('0'))
    avatar = Column(String, nullable=True)
