import streamlit as st

st.title("Check your garden here")

progress_text = "Milestone Progress"
my_bar = st.progress(0, text=progress_text)
milestone_progress = 50

my_bar.progress(milestone_progress, text=progress_text)