import streamlit as st

about_page = st.Page(
    page="navication/about_me.py",
    title="About Me",
    icon=":material/account_circle:",
    default=True,
)
project1_page = st.Page(
    page="navication/sales_dashboard.py",
    title="Sales Dashboard",
    icon=":material/bar_chart:",
)
project2_page = st.Page(
    page="navication/chatbot.py",
    title="Chat bot",
    icon=":material/smart_toy:",
)

pg = st.navigation(
    {
        "Info": [about_page],
        "Projects": [project1_page, project2_page],
    }
)

st.logo("assets/profile.JPG")
st.sidebar.text("Made by Oti:)")
pg.run()