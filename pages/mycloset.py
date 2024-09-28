import streamlit as st

st.title('Welcome to your virtual closet!')

if 'form_data' not in st.session_state:
    st.session_state.form_data = {
        'date_purchased': '',
        'brand': '',
        'last_time_worn': '',
    }

def save_form_data():
    st.session_state.form_data['date_purchased'] = st.session_state.date_purchased
    st.session_state.form_data['brand'] = st.session_state.brand
    st.session_state.form_data['last_time_worn'] = st.session_state.last_time_worn

def show_form():
    with st.form(key='my_form'):
        st.write('Enter the details of your clothing item below:')
        st.text_input('When did you buy this piece?', value=st.session_state.form_data['date_purchased'], key='date_purchased')
        st.text_input('What is the brand?', value=st.session_state.form_data['brand'], key='brand')
        st.text_input('When was the last time you wore this?', value=st.session_state.form_data['last_time_worn'], key='last_time_worn')
       
        submit_button = st.form_submit_button(label='Submit')
        if submit_button:
            save_form_data()

if st.button('Show form'):
    show_form()

st.write("Current form:")
st.write(st.session_state.form_data)