import streamlit as st
from streamlit_extras.colored_header import colored_header
from streamlit_extras.switch_page_button import switch_page
from lib.types.User import User
from annotated_text import annotated_text

if "user_info" not in st.session_state or not st.session_state["user_info"]:
    switch_page("Home")

user_data: User = st.session_state["user_info"]

colored_header(
    label=f"Chat around  @{user_data.name}",
    description="Go ahead, communicate.",
    color_name="orange-70",
)

prompt = st.chat_input("Say something")
if prompt:
    annotated_text((f"@{user_data.nickname}", f"{user_data.name}","#c09" ),)
    message = st.chat_message(f"@{user_data.nickname}", avatar=user_data.picture)
    message.write(f"{prompt}")