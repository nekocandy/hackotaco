import requests
import streamlit as st
from streamlit_echarts import st_echarts
from streamlit_extras.colored_header import colored_header
from streamlit_extras.let_it_rain import rain
from streamlit_extras.switch_page_button import switch_page

from lib.types.User import User

if "user_info" not in st.session_state or not st.session_state["user_info"]:
    switch_page("Home")

user_info: User = st.session_state["user_info"]
st.warning(
    "Echart component for streamlit has a bug with the latest version of streamlit for datetime and timeline graphs, so the graphs on this page won't load for the time being"  # noqa: E501
)
st.warning(
    "We will try to update this as soon as this is fixed, you can check the underlying [issue with the library here]()"  # noqa: E501
)

colored_header(
    label=f"Hack-o-Tacko @{user_info.name}",
    description="We at Hack-o-Tacko wish to enable hackers to navigate freely through the entirety of the hackathon without having too much hassle",  # noqa: E501
    color_name="yellow-70",
)

repo_name = st.text_input("Name of repository", "Hek")

response = requests.get(
    f"https://api.github.com/repos/{user_info.nickname}/{repo_name}/commits"
)


def get_all_commits(owner, repo_name):
    base_url = "https://api.github.com/repos/"
    url = f"{base_url}{owner}/{repo_name}/commits"
    commits = []
    page = 1

    while True:
        params = {"per_page": 100, "page": page}
        response = requests.get(url, params=params)

        if response.status_code == 200:
            data = response.json()
            if not data:
                break

            for commit in data:
                commits.append(
                    {
                        "message": commit["commit"]["message"],
                        "count": 1,
                        "date": commit["commit"]["author"]["date"],
                    }
                )
            page += 1
        else:
            st.error(f"Failed to fetch commits. Status code: {response.status_code}")
            return None

    return commits


d = get_all_commits(user_info.nickname, repo_name)
st.write(d)


options = {
    "title": {"text": "Commits"},
    "tooltip": {"trigger": "axis", "axisPointer": {"type": "shadow"}},
    "legend": {"data": ["Commits"]},
    "grid": {"left": "3%", "right": "4%", "bottom": "3%", "containLabel": True},
    "xAxis": {"type": "time"},
    "yAxis": {"type": "value"},
    "series": [
        {
            "name": "Commits",
            "type": "line",
            "data": d,
        }
    ],
}

st_echarts(options=options)
