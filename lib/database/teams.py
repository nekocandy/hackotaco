from .init import db


def create_team(owner: str, team_name: str, team_id: str):
    db.teams.insert_one({"owner": owner, "team_name": team_name, "team_id": team_id})
