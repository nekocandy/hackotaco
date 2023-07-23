from .init import db


def create_team(owner: str, team_name: str, team_id: str):
    db.teams.insert_one(
        {"owner": owner, "team_name": team_name, "team_id": team_id, "members": [owner]}
    )


def list_teams(user: str):
    return list(db.teams.find({"members": {"$in": [user]}}))


def get_team_info(team_id: str, username: str):
    return db.teams.find_one({"team_id": team_id, "members": {"$in": [username]}})

def set_team_data(team_id: str, data):
    db.teams.update_one({"team_id": team_id}, {"$set": data})
