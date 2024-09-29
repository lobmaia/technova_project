import streamlit as st
import pandas as pd 
import webbrowser

st.title("Welcome to the Community Garden!")
st.write("Here, you can find items that other users are selling")
st.write("You can also sell your own items")

with st.form("my_form"):
    st.text("Enter the details of the item you want to sell")
    your_name = st.text_input("Enter your name")
    date_purchased = st.text_area("When did you buy this item?")
    condition = st.text_input("Enter the condition of the item")
    brand = st.text_input("Enter the brand of the item")
    item_price = st.number_input("Enter item price")
    submit_button = st.form_submit_button("Submit")
if st.button("View your item details"):
        st.write("Your Name:", your_name)
        st.write("Date Purchased:", date_purchased)
        st.write("Condition:", condition)
        st.write("Brand:", brand)
        st.write("Selling Price:", item_price)

st.image("community_garden_images/gucci_shirt.png", width=300)
st.write("Robert Pattison wants to sell his shirt!")
if st.button("Show Robert's Shirt Details"):
    st.write("Owner: Robert Pattison")
    st.write("Date Purchased: January, 1920")
    st.write("Condition: New")
    st.write("Brand: Gucci")
    st.write("Selling Price: $200.00")
if st.button("Contact Robert"):
    webbrowser.open_new_tab("https://en.wikipedia.org/wiki/Robert_Pattinson")

st.image("community_garden_images/dress.jpg", width=300)
st.write("Sabrina Carpenter wants to sell her dress!")
if st.button("Show Sabrina's Dress Details"):
    st.write("Owner: Sabrina Carpenter")
    st.write("Date Purchased: March, 1865")
    st.write("Condition: Mild Wear")
    st.write("Brand: Dior")
    st.write("Selling Price: $128390.05")
if st.button("Contact Sabrina"):
    webbrowser.open_new_tab("https://en.wikipedia.org/wiki/Sabrina_Carpenter")

st.image("community_garden_images/goingoutfit.webp", width=300)
st.write("Bob Ross wants to sell his outfit!")
if st.button("Show Bob's Outfit Details"):
    st.write("Owner: Bob Ross")
    st.write("Date Purchased: June, 3049")
    st.write("Condition: Heavy Use")
    st.write("Brand: Bobber's Paints")
    st.write("Selling Price: $9.65")
if st.button("Contact Bob"):
    webbrowser.open_new_tab("https://en.wikipedia.org/wiki/Bob_Ross")

st.image("community_garden_images/hashtagelsa.jpg", width=300)
st.write("Jojo Siwa wants to sell her outfit!")
if st.button("Show Jojo's Outfit Details"):
    st.write("Owner: Jojo Siwa")
    st.write("Date Purchased: April, 2024")
    st.write("Condition: New")
    st.write("Brand: Jojo Bows")
    st.write("Selling Price: $0.50")
if st.button("Contact Jojo"):
    webbrowser.open_new_tab("https://en.wikipedia.org/wiki/JoJo_Siwa")
