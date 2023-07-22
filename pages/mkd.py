import streamlit as st
from streamlit_extras.colored_header import colored_header
from streamlit_extras.switch_page_button import switch_page

if "user_info" not in st.session_state or not st.session_state["user_info"]:
    switch_page("Home")
    
user_info = st.session_state["user_info"]

colored_header(
    label=f"Hack-o-Tacko @{user_info.name}",
    description="Here is the Markdown editor, to be able to view your devpost description side by side",
    color_name="violet-70",
)

col1, col2 = st.columns(2)
with col1:
  st.title("Markdown editor")
  txt = st.text_area("")
  # st.markdown(st.text_area("Description", "Description"))

with col2:
  st.title("Rendered .md")
  st.markdown(txt)

