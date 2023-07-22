from auth0_component import login_button
import streamlit as st

clientId = st.secrets["auth"]["client_id"]
domain = st.secrets["auth"]["domain"]

user_info = login_button(clientId, domain = domain)
st.write(user_info)
