import pymongo
import streamlit as st


@st.cache_resource
def init_connection():
    return pymongo.MongoClient(st.secrets["mongo"]["uri"])


client = init_connection()
db = client[st.secrets["mongo"]["db"]]
