import streamlit as st
from streamlit_extras.colored_header import colored_header
from streamlit_extras.switch_page_button import switch_page
from streamlit_extras.metric_cards import style_metric_cards

from lib.database.teams import list_teams
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
cols = st.columns(len(projects))

for col in range(len(cols)):
    project = projects[col]
    column = cols[col]
    column.metric(label="Name", value=project["team_name"], delta=project["team_id"])

style_metric_cards()
