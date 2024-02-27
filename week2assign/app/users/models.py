from flask_login import UserMixin
from app import get_db
from sqlalchemy.sql.expression import text
from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime

db = get_db()

class User(UserMixin, db.Model):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    username = Column(String(32), nullable=False)
    email = Column(String(64), unique=True, nullable=False)
    password = Column(String(100), nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow)

    def __repr__(self) -> str:
        return f"{self.username}"