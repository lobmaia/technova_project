'''from datasets import get_dataset_split_names

from datasets import load_dataset

dataset = load_dataset("zalando-datasets/fashion_mnist")

#train_dataset = dataset['train']

print ("zalando-datasets/fashion_mnist")'''''


# Step 1: Import Required Libraries
from datasets import load_dataset
from transformers import AutoFeatureExtractor, AutoModelForImageClassification, TrainingArguments, Trainer

# Step 2: Load the Fashion-MNIST dataset
fashion_mnist_dataset = load_dataset("fashion_mnist")

# Step 3: Initialize the feature extractor (to preprocess the images for the model)
feature_extractor = AutoFeatureExtractor.from_pretrained("google/vit-base-patch16-224")

# Step 4: Preprocess the dataset (convert images into the right format for the model)
def preprocess_fashion_mnist(examples):
    images = [image.convert("RGB") for image in examples["image"]]  # Convert grayscale images to RGB
    inputs = feature_extractor(images, return_tensors="pt")         # Apply the feature extractor
    inputs["labels"] = examples["label"]                            # Attach the labels to the images
    return inputs

# Apply the preprocessing function to the entire dataset
prepared_fashion_mnist_dataset = fashion_mnist_dataset.map(preprocess_fashion_mnist, batched=True)

# Step 5: Split the dataset into training and test sets
train_fashion_mnist_dataset = prepared_fashion_mnist_dataset["train"]
test_fashion_mnist_dataset = prepared_fashion_mnist_dataset["test"]

# Step 6: Load the pre-trained Vision Transformer (ViT) model for image classification
model = AutoModelForImageClassification.from_pretrained(
    "google/vit-base-patch16-224", 
    num_labels = len(fashion_mnist_dataset["train"].features["label"].names), ignore_mismatched_sizes = True  # Number of clothing categories
)

# Step 7: Define the training arguments
training_args = TrainingArguments(
    output_dir = "./results",            # Directory to save the model
    evaluation_strategy = "epoch",       # Evaluate the model after each epoch
    per_device_train_batch_size = 16,    # Batch size for training
    per_device_eval_batch_size = 16,     # Batch size for evaluation
    num_train_epochs = 3,                # Number of epochs to train the model
    save_strategy = "epoch",             # Save the model after each epoch
    logging_dir = "./logs",              # Directory to save logs
    logging_steps = 10,                  # Log training progress every 10 steps
)

# Step 8: Initialize the Trainer
trainer_fashion_mnist = Trainer(
    model = model,                          # The pre-trained ViT model
    args = training_args,                   # Training arguments
    train_dataset = train_fashion_mnist_dataset,  # Training dataset
    eval_dataset = test_fashion_mnist_dataset     # Testing dataset for evaluation
)

# Step 9: Train the model
trainer_fashion_mnist.train()

# Step 10: Evaluate the model
fashion_mnist_results = trainer_fashion_mnist.evaluate()

trainer_fashion_mnist.train()
trainer_fashion_mnist.save_model("./path_to_save_model")

model = AutoModelForImageClassification.from_pretrained("./path_to_save_model")







import streamlit as st
from PIL import Image
import pandas as pd
import numpy as np
import tensorflow as tf
import keras
from tensorflow.keras.preprocessing import image
from tensorflow.keras.applications.mobilenet_v2 import preprocess_input
from tensorflow.keras.models import load_model
from sklearn.metrics.pairwise import cosine_similarity
import random

# Load your trained clothing classifier model (change path if necessary)
model = load_model('model')

# Function to classify clothing type using the model
def classify_clothing_type(img, model):
    img = img.resize((224, 224))
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis = 0)
    img_array = preprocess_input(img_array)
    predictions = model.predict(img_array)
    predicted_class = np.argmax(predictions, axis = 1)
    clothing_labels = {0: 'Shirt', 1: 'Pants', 2: 'Jacket'}  # Example class mapping
    return clothing_labels[predicted_class[0]]

# Function to extract features using MobileNetV2 or any feature extraction model
def extract_features(img, feature_model):
    img = img.resize((224, 224))
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis = 0)
    img_array = preprocess_input(img_array)
    features = feature_model.predict(img_array)
    return features

# Initialize an empty DataFrame for the virtual closet
closet = pd.DataFrame(columns = ['ClothingID', 'ImagePath', 'Type', 'Color', 'Features', 'DateAdded'])

# Function to recommend complementary outfits based on category
def recommend_complementary_outfits(closet, target_category, complementary_categories, top_n = 2):
    target_items = closet[closet['Type'] == target_category]
    recommendations = []
    
    for idx, target_item in target_items.iterrows():
        target_features = target_item['Features']
        complementary_items = closet[closet['Type'].isin(complementary_categories)]
        
        complementary_items['Similarity'] = complementary_items['Features'].apply(
            lambda x: cosine_similarity([target_features], [x])[0][0]
        )
        
        top_recommendations = complementary_items.sort_values(by = 'Similarity', ascending = False).head(top_n)
        recommendations.append({
            'Target Item': target_item['ClothingID'],
            'Recommended Outfits': top_recommendations[['ClothingID', 'Type', 'Color', 'Similarity']]
        })
    
    return recommendations

# Streamlit App Layout
st.title("Your Virtual Closet with Automatic Recommendations")
st.write("Upload pictures of your clothes to automatically create your virtual closet and get outfit recommendations.")

# Upload images
uploaded_files = st.file_uploader("Upload clothes images", accept_multiple_files =True, type = ["jpg", "png"])

if uploaded_files:
    st.write("Processing uploaded images...")

    # Process each uploaded image
    for i, file in enumerate(uploaded_files):
        img = Image.open(file)

        # Use the trained model to classify the clothing type
        clothing_type = classify_clothing_type(img, model)
        
        # Extract features for recommendations
        features = extract_features(img, model)  # Assuming MobileNetV2 is used for feature extraction
        
        # Add the item to the virtual closet
        new_item = {
            'ClothingID': i + 1,
            'ImagePath': file.name,
            'Type': clothing_type,
            'Color': 'red',  
            'Features': features,
            'DateAdded': pd.Timestamp.now()
        }
        closet = closet.append(new_item, ignore_index = True)
    
    # Display the closet
    st.write("Your Virtual Closet:")
    st.dataframe(closet[['ClothingID', 'ImagePath', 'Type', 'Color']])

    def get_random_category(closet):
        unique_categories = closet['Type'].unique()
        random_category = random.choice(unique_categories)
        return random_category

    # Recommend outfits
    outfit_recommendations = recommend_complementary_outfits(
        closet,
        target_category = get_random_category,
        complementary_categories = get_random_category,
        top_n = 2
    )

    # Display outfit recommendations
    st.write("Outfit Recommendations:")
    for rec in outfit_recommendations:
        st.write(f"Outfit Recommendation for Shirt (ID: {rec['Target Item']}):")
        st.write(rec['Recommended Outfits'])

