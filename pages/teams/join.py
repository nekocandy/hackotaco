import streamlit as st
from streamlit_extras.colored_header import colored_header
from streamlit_extras.switch_page_button import switch_page

from lib.database.teams import add_user_to_team
from lib.types.User import User

if "user_info" not in st.session_state or not st.session_state["user_info"]:
    switch_page("Home")

user_info: User = st.session_state["user_info"]

colored_header(
    label="Join a Team",
    color_name="violet-70",
)

team_id = st.text_input("Team ID")
join_button = st.button("Team ID", disabled=len(team_id) <= 0)
if join_button:
  add_user_to_team(team_id, user_info.nickname)
  switch_page("List")
