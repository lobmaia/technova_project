import streamlit as st
import webbrowser

st.title('Sign In')
st.write('Please login')

username = st.text_input('Username')
#submit = st.button('Login')

st.page_link("home_page.py", label = 'login')

#st.page_link("pages/home_page.py", label = username)

'''if 'user_state' not in st.session_state:
    st.session_state.user_state = {
        'username': ' ',
        'password': ' ',
        'logged_in': False
    }

if not st.session_state.user_state['logged_in']:
    # Create login form
    st.write('Please login')
    username = st.text_input('Username')
    password = st.text_input('Password', type='password')
    submit = st.button('Login')


# Check if user is logged in
    if submit and st.session_state.user_state['logged_in'] == False:
        if username == 'admin' and password == '1234':
            st.session_state.user_state['username'] = username
            st.session_state.user_state['password'] = password
            st.session_state.user_state['logged_in'] = True
            st.write('You are logged in')
        else:
            st.warning('Invalid username or password')'''''