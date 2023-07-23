import streamlit as st
from streamlit_extras.colored_header import colored_header
from streamlit_extras.switch_page_button import switch_page
from nanoid import generate
from lib.database.teams import create_team

from lib.types.User import User

if "user_info" not in st.session_state or not st.session_state["user_info"]:
    switch_page("Home")

user_info: User = st.session_state["user_info"]

colored_header(
    label="Create a project",
    description="Create a project",  # noqa: E501
    color_name="violet-70",
)

project_id = generate()

project_name = st.text_input("Project Name")
create_button = st.button("Create Project", disabled=len(project_name) <= 0)
if create_button:
    create_team(owner=user_info.nickname, team_name=project_name, team_id=project_id)
    switch_page("list")
