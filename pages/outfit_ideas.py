'''import streamlit as st
import tensorflow as tf
import pandas as pd
import os
from tensorflow.keras.preprocessing import image
from tensorflow.keras.applications.mobilenet_v2 import preprocess_input, MobileNetV2
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

st.title("Need some outfit ideas!!!")


model = MobileNetV2(weights = 'imaginet', include_top = False, pooling = 'avg')


def extract_features(img_path):
    img = image.load_img(img_path, target_size = (224, 224))
    img_array = image.img_to_array(img)
    img_array = np.exapnd_dims(img_array, axis = 0)
    img_array = preprocess_input(img_array)
    features = model.predict(img_array)
    return features



def add_clothes(image_folder, clothing_df):
    for filename in os.listdir(image_folder):
        if filename.endswith(".jpg") or filename.endswith(".png"):
            image_path = os.path.joing(image_folder, filename)
            features = extract_features(image_path)

            new_item = {
                'ClothingID': len(clothing_df) + 1,
                'ImagePath': image_path,
                'Features': features,
                'Color': 'Unknown',  #add colour sorting algorithm
                'Type': 'Unknown',  #classifier?
                'WornCount': 0,
                'DateAdded': pd.Timestamp.now()
            }
            clothing_df = clothing_df.append(new_item, ignore_index = True)
    return clothing_df


#clothing_df = add_clothes('closet images', clothing_df)


def recommend_clothes(closet, top_n = 3):
    unworn_clothes = closet[closet['WornCount'] == 0]  # Find clothes not worn yet
    recommendations = unworn_clothes.head(top_n)  # Get top N unworn clothes
    return recommendations[['ClothingID', 'ImagePath', 'Color', 'Type', 'Style']]'''


import streamlit as st
from PIL import Image
import pandas as pd
import numpy as np
import tensorflow as tf
from sklearn.metrics.pairwise import cosine_similarity
from tensorflow.keras.preprocessing import image
from tensorflow.keras.applications.mobilenet_v2 import preprocess_input, MobileNetV2

# Load MobileNetV2 model
model = MobileNetV2(weights='imagenet', include_top = False, pooling = 'avg')

# Function to classify clothing type 
def classify_clothing_type(img):
    return 'Shirt'  # Placeholder for actual model or logic

# Function to extract dominant color
def extract_dominant_color(image):
    img = image.resize((50, 50))  # Resize the image for faster processing
    img_array = np.array(img)
    avg_color = np.mean(img_array, axis=(0, 1))  # Get the average color
    return avg_color

# Function to extract features using MobileNetV2
def extract_features(img):
    img = img.resize((224, 224))  # Resize the image to fit the model input
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)
    img_array = preprocess_input(img_array)
    features = model.predict(img_array)
    return features

# Initialize an empty DataFrame for the virtual closet
closet = pd.DataFrame(columns=['ClothingID', 'ImagePath', 'Type', 'Color', 'Features', 'DateAdded'])

# Streamlit App
st.title("Virtual Closet Builder")
st.write("Upload pictures of your clothes to automatically create your virtual closet.")

uploaded_files = st.file_uploader("Upload clothes images", accept_multiple_files=True, type=["jpg", "png"])

if uploaded_files:
    st.write("Processing uploaded images...")

    # Process each uploaded image
    for i, file in enumerate(uploaded_files):
        img = Image.open(file)
        
        # Automatically detect clothing type, color, and extract features
        clothing_type = classify_clothing_type(img)
        dominant_color = extract_dominant_color(img)
        features = extract_features(img)
        
        # Add to the closet
        new_item = {
            'ClothingID': i+1,
            'ImagePath': file.name,
            'Type': clothing_type,
            'Color': dominant_color,
            'Features': features,
            'DateAdded': pd.Timestamp.now()
        }
        closet = closet.append(new_item, ignore_index=True)
    
    # Display the closet
    st.write("Your Virtual Closet:")
    st.dataframe(closet[['ClothingID', 'ImagePath', 'Type', 'Color']])
