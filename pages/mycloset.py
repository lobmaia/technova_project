import streamlit as st

st.title("Welcome to your virtual closet!")

if 'form_data' not in st.session_state:
    st.session_state.form_data = {
        'date_purchased': '',
        'brand': '',
        'last_worn': '',
    }
def save_form_data(): 
    st.session_state.form_data['date_purchased'] = st.session_state.date_purchased
    st.session_state.form_data['brand'] = st.session_state.brand
    st.session_state.form_data['last_worn'] = st.session_state.last_worn

def show_form():
    with st.form(key='my_form'):
        st.text_input('Date Purchased', value=st.session_state.form_data['date_purchased'], key='date_purchased')
        st.text_input('Brand', value=st.session_state.form_data['brand'], key='brand')
        st.text_input('Last Worn', value=st.session_state.form_data['last_worn'], key='last_worn')
        submit = st.form_submit_button(label="Save info", on_click=save_form_data)
    st.write("Current form: ")
    st.write(st.session_state.form_data)

show_form()

"""
if 'images' not in st.session_state:
    st.session_state.images = [] """


"""
uploadedimages = st.file_uploader(label = "Upload your clothes here" , type=['png', 'jpg', 'jpeg'], accept_multiple_files=True)
if uploadedimages: 
    for file in uploadedimages: 
        st.session_state.images.append(file)

if st.session_state.images:
    for img in st.session_state.images:
        st.image(img, width=500)
        if st.button('Open Form'):
            show_form() """