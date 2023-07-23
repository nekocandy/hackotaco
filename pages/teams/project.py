import streamlit as st
from streamlit_extras.switch_page_button import switch_page

from lib.types.User import User

if "user_info" not in st.session_state or not st.session_state["user_info"]:
    switch_page("Home")

user_info: User = st.session_state["user_info"]

if "id" not in st.session_state or not st.session_state["id"]:
    switch_page("List")

id = st.session_state["id"]

st.title("Welcome to Hack-o-Taco 🌮")
st.subheader("This is your project.")
st.write(f"Project ID: {id}")
