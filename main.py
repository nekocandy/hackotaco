from auth0_component import login_button
import streamlit as st

clientId = st.secrets["auth"]["client_id"]
domain = st.secrets["auth"]["domain"]

if "user_info" not in st.session_state or not st.session_state["user_info"]:
  user_info = login_button(clientId, domain = domain)
  st.session_state["user_info"] = user_info

