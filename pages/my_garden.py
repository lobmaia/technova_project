import streamlit as st
from PIL import Image

st.title("Check Your Garden Here!")

#bar
progress_text = "Milestone Progress"
my_bar = st.progress(0, text=progress_text)
milestone_progress = 3

my_bar.progress(milestone_progress, text=progress_text)

#space
st.text("")
st.text("")

#overview
st.text("You have")
st.text(milestone_progress)
st.text ("flowers in your garden!")


#images
img=Image.open('flower_resized.png')
st.image([img,img,img])


