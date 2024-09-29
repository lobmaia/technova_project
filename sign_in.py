import streamlit as st
import webbrowser

st.title('Sign In')
st.write('Please login')

username = st.text_input('Username')
#submit = st.button('Login')

st.page_link("pages/home_page.py", label = 'Go to Home Page')
st.image("logo.png")