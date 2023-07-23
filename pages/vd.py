import streamlit as st
from streamlit_extras.colored_header import colored_header
from streamlit_extras.switch_page_button import switch_page
from lib.types.User import User
from streamlit_player import st_player
from streamlit_extras.stoggle import stoggle

if "user_info" not in st.session_state or not st.session_state["user_info"]:
    switch_page("Home")

user_data: User = st.session_state["user_info"]

colored_header(
    label=f"Welcome @{user_data.name}",
    description="Access Education Resources to kickstart your project.",
    color_name="blue-70",
)

vd_arr=["https://www.youtube.com/watch?v=mi9t8usEM3g&list=PLPDgudJ_VDUcgpSq_T1NdXaevNLawrOGo&index=1&pp=iAQB",
        
        "https://www.youtube.com/watch?v=fNVhjJ-K18c&list=PLPDgudJ_VDUcgpSq_T1NdXaevNLawrOGo&index=2&pp=iAQB",
        
        "https://www.youtube.com/watch?v=N5mq-cgnYSQ&list=PLPDgudJ_VDUcgpSq_T1NdXaevNLawrOGo&index=3&pp=iAQB",
        
        "https://www.youtube.com/watch?v=DnSTHKc1kIw&list=PLPDgudJ_VDUcgpSq_T1NdXaevNLawrOGo&index=4&pp=iAQB",
        
        "https://www.youtube.com/watch?v=fVFu1oKfe5E&list=PLPDgudJ_VDUcgpSq_T1NdXaevNLawrOGo&index=5&pp=iAQB",
        
        "https://www.youtube.com/watch?v=CIScyxuM708&list=PLPDgudJ_VDUcgpSq_T1NdXaevNLawrOGo&index=6&pp=iAQB",
        
        "https://www.youtube.com/watch?v=KEY82N2_PDk&list=PLPDgudJ_VDUcgpSq_T1NdXaevNLawrOGo&index=7&pp=iAQB",
        
        "https://www.youtube.com/watch?v=p4qdvP9HeoU&list=PLPDgudJ_VDUcgpSq_T1NdXaevNLawrOGo&index=8&pp=iAQB"]

with st.expander("See Part 1"):
  st.video(vd_arr[0])
  
with st.expander("See Part 2"):
  st.video(vd_arr[1])

with st.expander("See Part 3"):
  st.video(vd_arr[2])

with st.expander("See Part 4"):
  st.video(vd_arr[3])
  
with st.expander("See Part 5"):
  st.video(vd_arr[4])
  
with st.expander("See Part 6"):
  st.video(vd_arr[5])
  
with st.expander("See Part 7"):
  st.video(vd_arr[6])
  
with st.expander("See Part 8"):
  st.video(vd_arr[7])