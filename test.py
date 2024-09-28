import streamlit as st 
import pandas as pd 
import numpy as np

st.title('Hello')
st.page_link("pages/mycloset.py", label="look at your closet", icon="👚")
st.page_link("pages/mygarden.py", label="check your points", icon="🌼")
st.page_link("pages/communitygarden.py", label="visit the community garden", icon="🏡")
st.page_link("pages/outfitideas.py", label="need outfit ideas?", icon="👗")