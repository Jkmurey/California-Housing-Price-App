import streamlit as st
import pickle
import numpy as np
import pandas as pd

# Load the trained model
model = pickle.load(open("housing_model.pkl", "rb"))
st.title("California Housing Price Prediction App")
st.write("Enter housing details below to predict the house price.")

# User Inputs
MedInc = st.number_input("Median Income", value=3.0)
HouseAge = st.number_input("House Age", value=20)
AveRooms = st.number_input("No. of Rooms", value=5)
AveBedrms = st.number_input("No. of Bedrooms", value=1)
Population = st.number_input("Population", value=1000)
AveOccup = st.number_input("No. of Occupancy", value=3)
Latitude = st.number_input("Latitude", value=34.0)
Longitude = st.number_input("Longitude", value=-118.0)


# Convert inputs to array
features = pd.DataFrame({
    "MedInc": [MedInc],
    "HouseAge": [HouseAge],
    "AveRooms": [AveRooms],
    "AveBedrms": [AveBedrms],
    "Population": [Population],
    "AveOccup": [AveOccup],
    "Latitude": [Latitude],
    "Longitude": [Longitude]
})

# Predict button
if st.button("Predict Price"):
 prediction = model.predict(features)[0]
 price = prediction * 100000  # Convert to dollars
 st.success(f"Estimated House Price: ${price:,.2f}")
