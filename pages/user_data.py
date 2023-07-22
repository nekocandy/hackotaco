import streamlit as st
from streamlit_extras.colored_header import colored_header
from streamlit_extras.switch_page_button import switch_page

from lib.database.user import get_user_data
from lib.types.User import User

if "user_info" not in st.session_state or not st.session_state["user_info"]:
    switch_page("Home")


user_data: User = st.session_state["user_info"]
db_user_data = get_user_data(user_data.nickname)

st.image(user_data.picture, width=100)
colored_header(
    label=f"Welcome @{user_data.name}",
    description="Fill in the details to auto-fill into the devpost",
    color_name="green-70",
)
# st.header(f"Welcome {user_data.name}!")
college_name = st.text_input(
    "College Name", value=db_user_data.college_name if db_user_data else ""
)
if college_name:
    st.write(f"Your college name is {college_name}")
