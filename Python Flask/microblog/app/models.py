from app import db
from sqlalchemy import (
            Column, 
            Integer, 
            String, 
            DateTime, 
            ForeignKey)
from sqlalchemy.orm import relationship

class User(db.Model):
    id = Column(Integer, primary_key=True)
    name = Column(String(64), unique=True)
    email = Column(String(120), unique=True)
    posts = relationship('Post', backref='author', lazy='dynamic')
    
    def is_authenticated(self):
        return True
    
    def is_active(self):
        return True
    
    def is_anonymous(self):
        return False
    
    def get_id(self):
        return str(self.id)
    
    def __repr__(self):
        return '<User %r>' % (self.nickname)
    
class Post(db.Model):
    id = Column(Integer, primary_key=True)
    body = Column(String(140))
    timestamp= Column(DateTime)
    user_id = Column(Integer, ForeignKey('user.id'))
    
    def __repr__(self):
        return '<Post %r>' % (self.body)