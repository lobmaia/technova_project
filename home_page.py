import streamlit as st 
import pandas as pd 
import numpy as np

st.title('Hi')
st.page_link("pages/my_closet.py", label="look at your closet", icon="👚")
st.page_link("pages/my_garden.py", label="check your garden", icon="🌼")
st.page_link("pages/community_garden.py", label="visit the community garden", icon="🏡")
st.page_link("pages/outfit_ideas.py", label="need outfit ideas?", icon="👗")