import streamlit as st
from PIL import Image
import time
from streamlit_card import card
from streamlit_extras.badges import badge

st.set_page_config(layout="wide")
user_data = st.session_state["user_info"]

st.title("Welcome to Hack-o-Taco 🌮")
st.subheader("This is you.")

with open('styles\homestyle.css') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

a1, a2, a3 = st.columns(3)
a1.metric("Name", user_data.name, "Your Sexy Name")
a2.metric("Nickname", user_data.nickname, "The One'n'only")
a3.image(user_data.picture, width=150)

b2, b1 = st.columns(2)
b1 = st.button("Pomo!")

t1 = 1500
t2 = 300

if b1:
    with st.empty():
        while t1:
            mins, secs = divmod(t1, 60)
            timer = '{:02d}:{:02d}'.format(mins, secs)
            st.header(f"⏳ {timer}")
            time.sleep(1)
            t1 -= 1
            st.success("🔔 25 minutes is over! Time for a break!")

    with st.empty():
        while t2:
            # Start the break
            mins2, secs2 = divmod(t2, 60)
            timer2 = '{:02d}:{:02d}'.format(mins2, secs2)
            st.header(f"⏳ {timer2}")
            time.sleep(1)
            t2 -= 1
            st.error("⏰ 5 minute break is over!")

b2.write(f"{user_data.sub}")


# card(
#     title="Hello World!",
#     text="Some description",
#     image="http://placekitten.com/300/250",
#     url="https://www.google.com",
# )

# usrname = user_data.name
# usrnick = user_data.nickname
# usrmail = user_data.email

# v1, v2 = st.columns(2)
# v1.write(user_data.name)
# v2.write(user_data.nickname)
