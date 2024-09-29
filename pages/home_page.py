import streamlit as st 

# personalized home page
if 'logged_in' in st.session_state and st.session_state['logged_in']:
    st.title("Home")
    st.write(f"Hello, {st.session_state['username']}!")
    st.write('Our mission is to promote green sewlutions for overconsumption in clothing. We aim to help you reduce your carbon footprint by providing you with the tools to make sustainable choices in your wardrobe.')

# centered image
left_co, cent_co, last_co = st.columns(3)
with cent_co:
    st.image("sewstainable.png", width=200)

# links to nested pages
st.page_link("pages/my_closet.py", label="look at your closet", icon="👚")
st.page_link("pages/my_garden.py", label="check your garden", icon="🌼")
st.page_link("pages/community_garden.py", label="visit the community garden", icon="🏡")