from app.database.db import Base

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    username = Column(String(30), unique=True, nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    hashed_password = Column(String(100), nullable=False)

    urls = relationship("URL", back_populates="user", uselist=True)


class URL(Base):
    __tablename__ = "urls"

    id = Column(Integer, primary_key=True)
    short_url = Column(String, unique=True, nullable=False)
    original_url = Column(String, nullable=False)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=True)

    user = relationship("User", back_populates="urls", uselist=False)
