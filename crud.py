from sqlalchemy.orm import Session
from models import User

def create_user(db: Session,id:id, name: str, age: int,job:str,education:str):
    new_user = User(id=id,name=name, age=age,job=job,education=education)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

def get_users(db: Session):
    return db.query(User).all()

def get_user_by_name(db: Session, name: str):
    return db.query(User).filter_by(name=name).first()

def delete_user(db: Session,id:int):
    deletes=  db.query(User).filter_by(id=id).first()
    db.delete(deletes)
    db.commit()

def update_user_age(db: Session, user_id: int, new_age: int):
    user_to_update = db.query(User).filter_by(id=user_id).first()
    if user_to_update:
        user_to_update.age = new_age
        db.commit()
        return f"Kullanicinin yas bilgisi güncellendi. Yeni yaş: {new_age}"

