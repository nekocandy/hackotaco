from auth0_component import login_button
import streamlit as st

clientId = "1DGyKVUR5gelgxFd4sPt4zoirf9L1cGu"
domain = "hackshacks.us.auth0.com"

user_info = login_button(clientId, domain = domain)
st.write(user_info)

st.sidebar.header("User Info")
st.sidebar.button("Refresh")
st.sidebar.date_input("Date of Birth")
