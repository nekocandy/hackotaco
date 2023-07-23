import requests


def get_github_user_info(username: str):
    return requests.get(f"https://api.github.com/users/{username}").json()
