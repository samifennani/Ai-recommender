import streamlit as st
import pandas as pd

# Load database
df = pd.read_csv('products.csv')

# App title
st.title("AI Luxury Product Recommender")

# User input
st.sidebar.header("Customer Preferences")
gender = st.sidebar.selectbox("Gender", ["Male", "Female", "Other"])
product_type = st.sidebar.selectbox("Product Type", df['type'].unique())
color = st.sidebar.selectbox("Preferred Color", df['color'].unique())
budget = st.sidebar.slider("Budget (USD)", min_value=500, max_value=15000, step=500)

# Filter products
filtered = df[
    (df['type'] == product_type) &
    (df['color'] == color) &
    (df['price'] <= budget)
]

# Display recommendations
st.header("Recommended Products")
if not filtered.empty:
    for idx, row in filtered.iterrows():
        st.subheader(row['name'])
        st.image(row['image_url'], width=150)
        st.write(f"Price: ${row['price']}")
        st.write(row['description'])
else:
    st.write("No products match your preferences. Try adjusting your filters.")