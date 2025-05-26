import streamlit as st
import pickle
import pandas as pd

# Page setup
st.set_page_config(page_title="Health Classifier", page_icon="💪", layout="centered")

# Load model
with open("class.pkl", "rb") as f:
    model = pickle.load(f)

# Title
st.title("💪 Health Classification App")
st.write("Enter your weight and height to predict your health category.")

# Input fields
weight = st.text_input("Enter your weight (kg)", "")
height = st.text_input("Enter your height (cm)", "")

# Predict button
if st.button("Predict"):
    if weight and height:
        try:
            weight = float(weight)
            height = float(height)
            input_data = pd.DataFrame([[weight, height]], columns=["Weight", "Height"])
            result = model.predict(input_data)[0]
            st.success(f"Prediction: {result}")
        except:
            st.error("Please enter valid numbers.")
    else:
        st.warning("Fill in both weight and height.")