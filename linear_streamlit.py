# linear_streamlit.py
import streamlit as st
import pickle
import pandas as pd

# Load your model
with open("coffee_sales_model.pkl", "rb") as f:
    model = pickle.load(f)

# Load scaler if used
with open("scaler.pkl", "rb") as f:
    scaler = pickle.load(f)

# Load feature selector if used
with open("feature_selector.pkl", "rb") as f:
    selector = pickle.load(f)

st.title("☕ Coffee Shop Sales Prediction App")

# Input fields
st.header("Enter Coffee Order Details")
coffee_type = st.selectbox("Coffee Type", ["Espresso", "Latte", "Cappuccino"])
size = st.selectbox("Size", ["Small", "Medium", "Large"])
addons = st.multiselect("Add-ons", ["Extra Shot", "Syrup", "Whipped Cream"])
quantity = st.number_input("Quantity", min_value=1, max_value=50, value=1)

# Prepare input data
input_dict = {
    "Coffee_Type": coffee_type,
    "Size": size,
    "Addons": ", ".join(addons) if addons else "None",
    "Quantity": quantity
}

input_df = pd.DataFrame([input_dict])

# Feature selection if used
try:
    input_df = selector.transform(input_df)
except:
    pass  # If selector not used or columns match, skip

# Scaling if used
try:
    input_df = scaler.transform(input_df)
except:
    pass  # If scaler not used, skip

# Prediction button
if st.button("Predict Sales"):
    prediction = model.predict(input_df)
    st.success(f"Predicted Sale Price: ₹{prediction[0]:.2f}")

# Optional: safe rerun (avoid crash)
if st.button("Reset App"):
    st.experimental_rerun()  # Safe when inside a button
