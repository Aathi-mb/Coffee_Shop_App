# linear_streamlit.py
import streamlit as st
import pandas as pd
from sklearn.linear_model import LinearRegression

st.title("☕ Coffee Shop Sales Prediction")

# ======= Dummy model (no pickle) =======
# This is just for testing the Streamlit app
# You can replace with your trained pickle model later
model = LinearRegression()
# Train dummy model
df = pd.DataFrame({
    "Coffee_Type": [0,1,2],
    "Size": [0,1,2],
    "Quantity": [1,2,3],
    "Sale_Price": [100,150,200]
})
X = df[["Coffee_Type","Size","Quantity"]]
y = df["Sale_Price"]
model.fit(X, y)
# =======================================

# Inputs
st.header("Enter Order Details")
coffee_type = st.selectbox("Coffee Type", ["Espresso", "Latte", "Cappuccino"])
size = st.selectbox("Size", ["Small", "Medium", "Large"])
quantity = st.number_input("Quantity", min_value=1, max_value=50, value=1)

# Map categorical to numbers for dummy model
coffee_map = {"Espresso":0, "Latte":1, "Cappuccino":2}
size_map = {"Small":0, "Medium":1, "Large":2}

input_df = pd.DataFrame([{
    "Coffee_Type": coffee_map[coffee_type],
    "Size": size_map[size],
    "Quantity": quantity
}])

# Predict button
if st.button("Predict Sale Price"):
    prediction = model.predict(input_df)
    st.success(f"Predicted Sale Price: ₹{prediction[0]:.2f}")

# Reset button (safe way)
if st.button("Reset App"):
    st.experimental_rerun()
