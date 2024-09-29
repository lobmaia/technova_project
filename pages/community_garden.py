import streamlit as st
import pandas as pd 

st.title("Wanna buy some clothes??!!!")

st.image("community_garden_images/gucci_shirt.png", width=300)
st.write("Robert Pattison wants to sell his shirt!")
st.session_state.robert_data = {
    'Owner': 'Robert Pattison',
    'Date Purchased': 'September, 2019',
    'Condition': 'New',
    'Brand': 'Gucci',
    'Selling Price': '$48.00',
    'Contact Info': '911',
}
st.write(st.session_state.robert_data)

st.image("community_garden_images/dress.jpg", width=300)
st.write("Sabrina Carpenter wants to sell her dress!")
st.session_state.sabrina_data = {
    'Owner': 'Sabrina Carpenter',
    'Date Purchased': 'January, 1920',
    'Condition': 'Mild Wear',
    'Brand': 'Doir',
    'Selling Price': '$2348.00',
    'Contact Info': '1800-GOT-STYLE',
}
st.write(st.session_state.sabrina_data)

st.image("community_garden_images/goingoutfit.webp", width=300)
st.write("Bob Ross wants to sell his outfit!")
st.session_state.bob_data = {
    'Owner': 'Bob Ross',
    'Date Purchased': 'March, 1422',
    'Condition': 'Heavily Used',
    'Brand': 'Walmart',
    'Selling Price': '$2.00',
    'Contact Info': 'bobby@hotmail.com',
}
st.write(st.session_state.bob_data)

st.image("community_garden_images/hashtagelsa.jpg", width=300)
st.write("Jojo Siwa wants to sell her dress!")
st.session_state.jojo_data = {
    'Owner': 'Jojo Swia',
    'Date Purchased': 'December, 2023',
    'Condition': 'New',
    'Brand': 'Jojo Bows',
    'Selling Price': '$63008.00',
    'Contact Info': 'jojo@jojo.com',
}
st.write(st.session_state.jojo_data)