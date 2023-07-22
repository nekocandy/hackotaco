import streamlit as st

if "user_info" not in st.session_state or not st.session_state["user_info"]:
    st.write("You are not logged in.")
else:
  st.write(st.session_state["user_info"])
