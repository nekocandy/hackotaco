import streamlit as st
from streamlit_extras.colored_header import colored_header
from streamlit_extras.let_it_rain import rain
from streamlit_extras.switch_page_button import switch_page
import requests

if "user_info" not in st.session_state or not st.session_state["user_info"]:
    switch_page("Home")

rain(
    emoji="💻",
    font_size=40,
    falling_speed=10,
    animation_length="infinite",
)

user_info = st.session_state["user_info"]

colored_header(
    label=f"Hack-o-Tacko @{user_info.name}",
    description="We at Hack-o-Tacko wish to enable hackers to navigate freely through the entirety of the hackathon  without having too much hassle",
    color_name="yellow-70",
)

repo_name = st.text_input('Name of repository', 'Repository Name')

response = requests.get(f"https://api.github.com/repos/{user_info.nickname}/{repo_name}/commits?per_page=1")

if response.status_code == 200:
  st.write("Repository you are hacking with this weekend is", repo_name)
else:
  st.write(f"{response.status_code} repository not found")
  
