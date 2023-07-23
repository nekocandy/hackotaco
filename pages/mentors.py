import streamlit as st
from streamlit_card import card
from streamlit_extras.colored_header import colored_header
from streamlit_extras.let_it_rain import rain
from streamlit_extras.switch_page_button import switch_page

from lib.database.user import get_all_users
from lib.github import get_github_user_info
from lib.types.User import User

if "user_info" not in st.session_state or not st.session_state["user_info"]:
    switch_page("Landing")

user_info: User = st.session_state["user_info"]

colored_header(
    label=f"Look for Mentors @{user_info.name}",
    description="We at Hack-o-Tacko wish to enable hackers to look for mentors and get help from them without much hassle.",  # noqa: E501
    color_name="yellow-70",
)


def rain_pfp():
    rain("💡", animation_length="2s")


users = get_all_users()
card_data = []
for user in users:
    github_info = get_github_user_info(user["username"])
    card_data.append(
        {
            "name": github_info["name"],
            "username": github_info["login"],
            "college_name": user.get("college_name", "N/A"),
            "github_url": github_info["html_url"],
            "followers": github_info["followers"],
            "following": github_info["following"],
            "avatar_url": github_info["avatar_url"],
        }
    )
columns = st.columns(len(card_data))
for i in range(len(card_data)):
    info = card_data[i]
    with columns[i].container():
        card(
            title=info["name"],
            text=f"Org: {info['college_name']}\n|{info['followers']} Followers | Available for Discussion",  # noqa: E501
            image=info["avatar_url"],
            url=info["github_url"],
            on_click=rain_pfp,
        )
