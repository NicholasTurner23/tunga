from app import get_db, get_ma
from sqlalchemy.sql.expression import text
from sqlalchemy import Column, Integer, String, Text, ForeignKey, DateTime
from sqlalchemy.sql.sqltypes import TIMESTAMP
from sqlalchemy.orm import relationship
from app.users.models import User
from datetime import datetime
from marshmallow import fields

db = get_db() 
ma = get_ma()
class BlogPost(db.Model):
    __tablename__ = "posts"
    id = Column(Integer, primary_key=True)
    title = Column(String(128), nullable=False)
    body = Column(Text, nullable=False)
    author_id = Column(Integer, ForeignKey("users.id", ondelete='CASCADE'), nullable=False)
    author = relationship(User, backref='posts')
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow)

    def __repr__(self) -> str:
        return f"BlogPost('{self.title}','{self.author}','{self.created_at}')"
    

class BlogPostSchema(ma.SQLAlchemyAutoSchema):
    author_id = fields.Integer()
    author = fields.Nested('UserSchema')
    class Meta:
        model = BlogPost
        load_instance = True
        sqla_session = db.session
        exclude = ('author',)

blogpost_schema = BlogPostSchema()
blogposts_schema = BlogPostSchema(many=True)