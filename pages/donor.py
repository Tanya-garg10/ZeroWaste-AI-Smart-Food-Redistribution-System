import streamlit as st
from model import predict_surplus

st.set_page_config(page_title="Donor Portal", page_icon="🏪")

st.title("🏪 Donor Portal")
st.write("Enter food details to predict surplus food.")

day = st.selectbox(
    "Day",
    ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
)

meal = st.selectbox(
    "Meal Type",
    ["Breakfast", "Lunch", "Dinner"]
)

prepared = st.number_input("Prepared Quantity", min_value=0, value=100)
consumed = st.number_input("Consumed Quantity", min_value=0, value=80)

weather = st.selectbox(
    "Weather",
    ["Sunny", "Rainy", "Cloudy"]
)

event = st.selectbox(
    "Event",
    ["Yes", "No"]
)

if st.button("Predict Surplus"):
    if consumed > prepared:
        st.error("Consumed quantity cannot be greater than prepared quantity.")
    else:
        result = predict_surplus(day, meal, prepared, consumed, weather, event)
        st.success(f"Predicted Surplus Food: {result} units")

        meals_saved = round(result / 2, 1)
        st.info(f"Estimated Meals That Can Be Saved: {meals_saved}")