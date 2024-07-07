import streamlit as st
import Home
import Input
import Chart

PAGES = {
    "Home": Home,
    "Input": Input,
    "Chart": Chart
}

st.sidebar.title('Navigation')
selection = st.sidebar.radio("Go to", list(PAGES.keys()))

page = PAGES[selection]
page.app()

