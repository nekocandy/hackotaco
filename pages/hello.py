import streamlit as st
from streamlit_extras.colored_header import colored_header
from streamlit_extras.let_it_rain import rain

rain(
    emoji="$",
    font_size=40,
    falling_speed=10,
    animation_length="infinite",
)

colored_header(
    label="Hey Hacker",
    description="We at Hack0Tack0 wish to enable hackers to navigate freely through the entirety of the hackathon  without having too much hassle",
    color_name="yellow-70",
)


if "user_info" not in st.session_state or not st.session_state["user_info"]:
    st.write("You are not logged in.")
else:
  st.write(st.session_state["user_info"])
