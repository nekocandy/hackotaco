import streamlit as st
from streamlit_extras.colored_header import colored_header
from streamlit_extras.switch_page_button import switch_page
from nanoid import generate
from lib.database.teams import create_team, list_teams

from lib.types.User import User

if "user_info" not in st.session_state or not st.session_state["user_info"]:
    switch_page("Home")

user_info: User = st.session_state["user_info"]

colored_header(
    label=f"Projects for {user_info.name}",
    description="All projects you are a part of!",
    color_name="violet-70",
)

projects = list_teams(user_info.nickname)

st.write(projects)
