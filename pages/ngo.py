import streamlit as st

st.set_page_config(page_title="NGO Portal", page_icon="🤝")

st.title("🤝 NGO Matching Portal")
st.write("Nearby NGOs can view and accept available food pickups.")

surplus_food = {
    "provider": "Sunrise Hostel Mess",
    "food_type": "Cooked Meal",
    "quantity": "25 units",
    "pickup_time": "7:00 PM - 8:00 PM",
    "location": "Meerut"
}

st.subheader("Available Surplus Food")
st.write(f"**Food Provider:** {surplus_food['provider']}")
st.write(f"**Food Type:** {surplus_food['food_type']}")
st.write(f"**Quantity:** {surplus_food['quantity']}")
st.write(f"**Pickup Time:** {surplus_food['pickup_time']}")
st.write(f"**Location:** {surplus_food['location']}")

st.divider()

ngos = [
    {"name": "Hope Shelter", "distance": 2.1, "status": "Available"},
    {"name": "Food For All", "distance": 3.4, "status": "Available"},
    {"name": "Care Kitchen", "distance": 5.0, "status": "Available"},
]

st.subheader("Nearby NGOs")

for i, ngo in enumerate(ngos):
    st.write(f"### {ngo['name']}")
    st.write(f"Distance: {ngo['distance']} km")
    st.write(f"Status: {ngo['status']}")

    if st.button(f"Accept Pickup - {ngo['name']}", key=f"ngo_{i}"):
        st.success(f"{ngo['name']} has accepted the pickup request.")
    st.divider()