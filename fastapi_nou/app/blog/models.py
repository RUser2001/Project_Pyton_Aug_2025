from sqlalchemy import Column, Integer, String, ForeignKey, Text
from app.blog.database import Base
from sqlalchemy.orm import relationship

class Blog(Base):
    __tablename__ = 'blogs'

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    body = Column(String, nullable=False)
    user_id= Column(Integer, ForeignKey('users.id'), nullable=False)

    creator = relationship("User", back_populates="blogs", lazy="joined")

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False, unique=True)
    password = Column(String, nullable=False)

    blogs = relationship("Blog", back_populates="creator")