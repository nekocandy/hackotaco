import pandas as pd
import streamlit as st
from streamlit_extras.colored_header import colored_header
from streamlit_extras.image_in_tables import table_with_images
from streamlit_extras.switch_page_button import switch_page

from lib.database.teams import get_team_info, set_team_data
from lib.github import get_github_user_info
from lib.types.User import User

if "user_info" not in st.session_state or not st.session_state["user_info"]:
    switch_page("Home")

user_info: User = st.session_state["user_info"]

if "id" not in st.session_state or not st.session_state["id"]:
    switch_page("List")

st.set_page_config(layout="wide")
id = st.session_state["id"]

project_data = get_team_info(id, user_info.nickname)
members = project_data["members"]
github_members = []

for member in members:
    user_data = get_github_user_info(member)
    github_members.append(
        {
            "avatar": user_data["avatar_url"],
            "name": user_data["name"],
            "url": user_data["html_url"],
        }
    )


colored_header(
    label=f"Hack-o-Tacko @{project_data['team_name']}",
    description="Your Team's Project Page!",  # noqa: E501
    color_name="yellow-70",
)


def render(title, key, value):
    st.header(title)
    text = st.text_area(title, value)
    st.header("Rendered Markdown")
    st.markdown(text)
    if text: 
        set_team_data(id, {key: text})


st.info(
    f"Team ID: **{project_data['team_id']}**\n\nSend this ID to your group member to join this team"  # noqa: E501
)  # noqa: E501

team_info, markdown = st.tabs(["Team Info", "Project Information"])

with team_info:
    df = pd.DataFrame.from_dict(github_members)
    df_html = table_with_images(df, url_columns=("avatar",))
    st.header("Team")
    st.markdown(df_html, unsafe_allow_html=True)

with markdown:
    st.header("Project Information")
    (
        inspiration,
        what_it_does,
        how_we_built_it,
        challenges_we_ran_into,
        accomplishments,
        what_we_learned,
        what_is_next,
    ) = st.tabs(
        [
            "Inspiration",
            "What it does",
            "How we built it",
            "Challenges",
            "Accomplishments that we're proud of",
            "What we learned",
            "What's next",
        ]
    )  # noqa: E501

    with inspiration:
        render("Inspiration", "inspiration", project_data.get("inspiration", ""))

    with what_it_does:
        render("What it does", "what_it_does", project_data.get("what_it_does", ""))

    with how_we_built_it:
        render(
            "How we built it",
            "how_we_built_it",
            project_data.get("how_we_built_it", ""),
        )  # noqa: E501

    with challenges_we_ran_into:
        render(
            "Challenges",
            "challenges_we_ran_into",
            project_data.get("challenges_we_ran_into", ""),
        )

    with accomplishments:
        render(
            "Accomplishments",
            "accomplishments",
            project_data.get("accomplishments", ""),
        )

    with what_we_learned:
        render(
            "What we learned",
            "what_we_learned",
            project_data.get("what_we_learned", ""),
        )

    with what_is_next:
        render("What's next", "what_is_next", project_data.get("what_is_next", ""))
