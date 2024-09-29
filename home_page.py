import streamlit as st 
import pandas as pd 
import numpy as np

st.title('Welcome to Sewstainability!')
st.write('Our mission is to promote green sewlutions for overconsumption in clothing. We aim to help you reduce your carbon footprint by providing you with the tools to make sustainable choices in your wardrobe.')
st.page_link("pages/my_closet.py", label="look at your closet", icon="👚")
st.page_link("pages/my_garden.py", label="check your garden", icon="🌼")
st.page_link("pages/community_garden.py", label="visit the community garden", icon="🏡")
st.page_link("pages/outfit_ideas.py", label="need outfit ideas?", icon="👗")