from .init import db


def get_data(username: str):
    user_data = db.users.find_one({"username": username})
    if user_data:
        return user_data
    else:
        return None
