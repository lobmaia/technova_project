import streamlit as st
import webbrowser

st.title('Sign In')
st.write('Please login')

# collecting data
username = st.text_input('Enter username')

# The actual sign in; also takes user to personalized home page
if st.button("Sign In"):
    # Set session state to logged in
    st.session_state['logged_in'] = True
    st.session_state['username'] = username
    st.page_link("pages/home_page.py", label = 'Go to Home Page')

st.image("logo.png")