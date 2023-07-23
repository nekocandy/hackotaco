import streamlit as st
from streamlit_extras.colored_header import colored_header
from streamlit_extras.switch_page_button import switch_page

if "user_info" not in st.session_state or not st.session_state["user_info"]:
    switch_page("Home")

st.set_page_config(layout="wide") 
user_info = st.session_state["user_info"]

colored_header(
    label=f"Hack-o-Tacko @{user_info.name}",
    description="Here is the Markdown editor, to be able to view your devpost description side by side",
    color_name="violet-70",
)

default_value = """
## Inspiration

## What it does

## How we built it

## Challenges we ran into

## Accomplishments that we're proud of

## What we learned

## What's next for HackerHacker
"""

col1, col2 = st.columns(2, gap="medium")
with col1:
    st.write("Markdown editor")
    txt = st.text_area("", value=default_value.strip(), height=600)

with col2:
    st.write("Rendered .md")
    st.markdown(txt)
