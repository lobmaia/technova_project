import streamlit as st

st.title("Here's your closet")

picture = st.camera_input("Take a pic of your clothes")

if picture:
    st.image(picture)

