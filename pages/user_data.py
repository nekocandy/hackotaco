import streamlit as st

from streamlit_extras.switch_page_button import switch_page

if "user_info" not in st.session_state or not st.session_state["user_info"]:
    switch_page("Home")

st.write(st.session_state["user_info"].email)
