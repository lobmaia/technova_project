import streamlit as st

st.title("Here's your closet")

st.text("Take a picture of your outfit!") 

if 'images' not in st.session_state:
    st.session_state.images = []

uploadedimages = st.file_uploader("Upload an image", type=['png', 'jpg', 'jpeg'], accept_multiple_files=True)
if uploadedimages: 
    for file in uploadedimages: 
        st.session_state.images.append(file)
        st.image(file, width=500)