from app import db
from sqlalchemy import Column, Integer, String

class User(db.Model):
    id = Column(Integer, primary_key=True)
    name = Column(String(64), unique=True)
    email = Column(String(120), unique=True)
    
    def __repr__(self):
        return '<User %r>' %(self.nickname)