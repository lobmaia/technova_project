import streamlit as st

st.title('Welcome to your virtual closet!')

#initialize form data 
if 'form_data' not in st.session_state:
    st.session_state.form_data = {
        'date_purchased': '',
        'brand': '',
        'last_time_worn': '',
    }

#save the data from the form 
def save_form_data():
    st.session_state.form_data['date_purchased'] = st.session_state.date_purchased
    st.session_state.form_data['brand'] = st.session_state.brand
    st.session_state.form_data['last_time_worn'] = st.session_state.last_time_worn

#collect data from the form 
def show_form():
    with st.form(key='my_form'):
        st.write('Enter the details of your clothing item below:')
        st.text_input('When did you buy this piece?', value = st.session_state.form_data['date_purchased'], key='date_purchased')
        st.text_input('What is the brand?', value=st.session_state.form_data['brand'], key = 'brand')
        st.text_input('When was the last time you wore this?', value=st.session_state.form_data['last_time_worn'], key = 'last_time_worn')
       
        submit_button = st.form_submit_button(label='Submit', on_click=save_form_data)
        save_form_data()

#view the data collected from the form 
def view_clothing_details():
    st.write('Clothing details:')
    st.write(st.session_state.form_data)

if 'images' not in st.session_state:
    st.session_state.images = [] 

uploadedimages = st.file_uploader("Upload an image of your clothing item", type=['jpg', 'jpeg', 'png'], accept_multiple_files=True)
st.image(uploadedimages, width=200)
if st.button('Update clothing details'): 
    show_form()
if st.button('View clothing details'):
    view_clothing_details()