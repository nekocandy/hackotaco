from .init import db


def get_user_data(username: str):
    user_data = db.users.find_one({"username": username})
    if user_data:
        return user_data
    else:
        return None

def get_all_users():
    return list(db.users.find({}))

def set_user_data(username: str, data: dict):
    db.users.update_one({"username": username}, {"$set": data}, upsert=True)
