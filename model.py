import pandas as pd
import streamlit as st
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split

df = pd.read_csv("real_estate_500.csv")

X = df.drop("Price_INR", axis=1)
y = df["Price_INR"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

model = RandomForestRegressor()
model.fit(X_train, y_train)

st.title("🏡 House Price Predictor")

area = st.number_input("Area (sqft)", min_value=500)
bedrooms = st.number_input("Bedrooms", min_value=1)
bathrooms = st.number_input("Bathrooms", min_value=1)
age = st.number_input("Property Age", min_value=0)
parking = st.number_input("Parking Spaces", min_value=0)
location = st.slider("Location Score", 1, 10)

if st.button("Predict Price"):
    house = [[area, bedrooms, bathrooms, age, parking, location]]
    prediction = model.predict(house)

    st.success(f"Predicted Price: ₹{prediction[0]:,.0f}")
