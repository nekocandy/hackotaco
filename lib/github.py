import requests
import streamlit as st

def get_github_user_info(username: str):
    return requests.get(f"https://api.github.com/users/{username}", headers={
        "Accept": "application/vnd.github.v3+json",
        "Authorization": f"Bearer {st.secrets['gh']['token']}"
    }).json()
