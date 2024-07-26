from sqlalchemy import Column, Integer, String, CHAR
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True,)
    name = Column(String)
    age = Column(Integer)
    job = Column(String)
    education = Column(String)
    def __repr__(self):
        return f"<User(name='{self.name}', age={self.age}), job={self.job}, education={self.education}>"
    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'age': self.age,
            'job': self.job, 
            'education': self.education
        }