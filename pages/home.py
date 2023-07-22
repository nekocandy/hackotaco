import typing
import streamlit as st
from auth0_component import login_button
from streamlit_extras.switch_page_button import switch_page
from lib.types.User import User

clientId = st.secrets["auth"]["client_id"]
domain = st.secrets["auth"]["domain"]

if "user_info" not in st.session_state or not st.session_state["user_info"]:
    user_info = login_button(clientId, domain=domain)
    if not not user_info:
        st.session_state["user_info"] = User.from_dict(user_info)
else:
    user_data: typing.Union[User, bool] = st.session_state["user_info"]
    if not not user_data:
        st.write(f"Welcome {user_data.name}!")

want_to_contribute = st.button("I want to contribute!")
if want_to_contribute:
    switch_page("Hello")
