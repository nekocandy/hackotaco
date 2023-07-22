import typing
import streamlit as st
from auth0_component import login_button
from streamlit_extras.switch_page_button import switch_page
from lib.types.User import User
from lib.database.user import get_user_data

clientId = st.secrets["auth"]["client_id"]
domain = st.secrets["auth"]["domain"]

if "user_info" not in st.session_state or not st.session_state["user_info"]:
    user_info = login_button(clientId, domain=domain)
    if not not user_info:
        typed_user = User.from_dict(user_info)
        user_data_from_db = get_user_data(typed_user.nickname)
        st.session_state["user_info"] = typed_user
        if not user_data_from_db:
            switch_page("User Data")

        user_college_name = user_data_from_db.get("college_name", None)
        if not user_college_name or len(user_college_name) == 0:
            switch_page("User Data")
else:
    user_data: typing.Union[User, bool] = st.session_state["user_info"]
    if not not user_data:
        st.write(f"Welcome {user_data.name}!")
