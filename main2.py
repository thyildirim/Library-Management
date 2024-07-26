import json
from config import engine, SessionLocal
from models import Base
from crud import create_user, get_users, get_user_by_name, delete_user, update_user_age
import requests

def init_db():
    Base.metadata.create_all(engine)


def main():
    global age, name,job,education
    init_db()
    db = SessionLocal()

    print("\n\nMenü",
          "1) Kullanici kaydi",
          "2) Kendi Kullanici bilgileri getirme",
          "3) Kullanici güncelleme",
          "4) Kullanici silme",
          "5) Tüm kayitlari listeleme ",
          "6) Geri dön")

    while True:
        choose = input("Lütfen tercihinizi yapiniz: \n")
        if choose == '1':
            id = input("Select your id ")
            name = input("Enter name for new user (or 'exit' to quit): ")
            age = int(input(f"Enter age for {name}: "))
            job = input("Enter your job ")
            education = input("Enter educat. info ")
            create_user((db),id, name, age,job, education)
            print(f"User {name} created successfully.")
            save_to_json(db)
        elif choose == '2':
            user = get_user_by_name(db, name)
            print(f"User found in JSON format: {json.dumps(user.to_dict(), indent=4)}")

        elif choose == '3':
            id = int(input("Enter your id"))
            update_age = int(input("Enter new age"))
            update_user_age(db, id, update_age)
            print("\n\n")
            save_to_json(db)
        elif choose == '4':
            delete_user_id = int(input("Enter id for delete user (or 'exit' to quit)"))
            delete_user(db, delete_user_id)
            save_to_json(db)
        elif choose == '5':
            all_user = input("Enter all user for get all user (or 'exit' to quit)")
            print(get_users(db))
        elif choose == 'exit':
            break


    
def save_to_json(db):
    # Tüm kullanıcıları getir
    users = get_users(db)
    users_dict = [user.to_dict() for user in users]
    # Tüm kullanıcıları JSON formatında kaydet
    with open('users.json', 'w') as file:
        json.dump(users_dict, file, indent=4)

    db.close()

if __name__ == '__main__':
    main()