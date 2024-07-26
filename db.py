from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine('postgresql://postgres:1234@localhost:5432/Taha', echo=True)

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)
    age = Column(Integer)
    job = Column(String)
    education = Column(String)
    def __repr__(self):
        return f"<User(name='{self.name}', age={self.age}), job={self.job}, education={self.education}>"



Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

session.commit()
users = session.query(User).all()
print(users)
