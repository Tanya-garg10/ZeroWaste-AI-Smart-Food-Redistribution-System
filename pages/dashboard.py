import streamlit as st
import pandas as pd

st.set_page_config(page_title="Impact Dashboard", page_icon="📊")

st.title("📊 Impact Dashboard")
st.write("Track food waste reduction and social impact.")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Meals Saved", "120")

with col2:
    st.metric("Food Rescued (kg)", "60")

with col3:
    st.metric("NGOs Connected", "3")

st.subheader("Weekly Food Rescue Trend")

chart_data = pd.DataFrame({
    "Day": ["Mon", "Tue", "Wed", "Thu", "Fri"],
    "Food Rescued": [10, 20, 15, 25, 30]
})

st.line_chart(chart_data.set_index("Day"))

st.subheader("Surplus Food Distribution")

distribution_data = pd.DataFrame({
    "Category": ["Hostels", "Restaurants", "Events"],
    "Quantity": [35, 20, 25]
})

st.bar_chart(distribution_data.set_index("Category"))

st.subheader("Impact Summary")
st.write("""
- Reduced daily food waste through early surplus prediction  
- Connected food providers with nearby NGOs  
- Improved chances of timely redistribution before spoilage  
- Demonstrated measurable social and environmental impact  
""")