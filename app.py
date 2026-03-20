import streamlit as st
from model import predict_surplus

st.set_page_config(page_title="ZeroWaste AI", layout="wide")

st.title("🍽️ ZeroWaste AI")
st.subheader("Predict & Redistribute Surplus Food")

# Sidebar
menu = st.sidebar.selectbox("Menu", ["Home", "Donor", "NGO", "Dashboard"])

# ---------------- HOME ----------------
if menu == "Home":
    st.write("### Welcome to ZeroWaste AI 🚀")
    st.write("""
    AI-powered platform that predicts surplus food and connects it with NGOs 
    to reduce waste and fight hunger.
    """)

# ---------------- DONOR ----------------
elif menu == "Donor":
    st.write("### 🏪 Donor Portal")

    col1, col2 = st.columns(2)

    with col1:
        day = st.selectbox("Day", ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"])
        meal = st.selectbox("Meal Type", ["Breakfast","Lunch","Dinner"])
        prepared = st.number_input("Prepared Quantity", min_value=0, value=100)

    with col2:
        consumed = st.number_input("Consumed Quantity", min_value=0, value=80)
        weather = st.selectbox("Weather", ["Sunny","Rainy","Cloudy"])
        event = st.selectbox("Event", ["Yes","No"])

    if st.button("🔍 Predict Surplus"):
        if consumed > prepared:
            st.error("Consumed quantity cannot be greater than prepared quantity ❌")
        else:
            result = predict_surplus(day, meal, prepared, consumed, weather, event)
            
            st.success(f"🍲 Predicted Surplus Food: {result} units")

            meals = round(result / 2, 1)
            st.info(f"🍽️ Estimated Meals Saved: {meals}")

# ---------------- NGO ----------------
elif menu == "NGO":
    st.write("### 🤝 NGO Matching")

    ngos = [
        {"name": "Hope Shelter", "distance": 2},
        {"name": "Food For All", "distance": 3},
        {"name": "Care Kitchen", "distance": 5}
    ]

    for i, ngo in enumerate(ngos):
        st.write(f"🏠 {ngo['name']} - {ngo['distance']} km away")

        if st.button(f"Accept Pickup - {ngo['name']}", key=i):
            st.success(f"{ngo['name']} has accepted the pickup ✅")

# ---------------- DASHBOARD ----------------
elif menu == "Dashboard":
    st.write("### 📊 Impact Dashboard")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("Meals Saved", "120")

    with col2:
        st.metric("Food Rescued (kg)", "60")

    with col3:
        st.metric("NGOs Connected", "3")

    st.write("### 📈 Weekly Trend")
    st.bar_chart([10, 20, 30, 25, 40])