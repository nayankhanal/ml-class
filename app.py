import streamlit as st
import requests

st.title("Height Predictor")

weight = st.number_input("Enter Weight")

if st.button("Predict Height"):
    response = requests.post("http://localhost:8000/predict", json={'weight': weight})
    # response = requests.post("https://nayankhanal-height-predictor.hf.space/predict", json={'weight': weight})
    height = response.json()['predicted_height']
    # height = response
    st.success(f"Predicted Height: {height}")