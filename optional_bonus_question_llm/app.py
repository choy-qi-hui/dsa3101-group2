import streamlit as st
from agent import recommender, reviewer
import random

# Set up Streamlit interface
st.title("Natural Language Product Search")
st.write("Search for products using natural language!")

PRODUCTS_EXAMPLE = ["Owala Water Bottle", "Sony Headphones", "SD Card Reader", "Kindle", "Guitar Picks", "Canon Cameras", "Shower Gel"]

with st.form("Product seach"):
    item = random.choice(PRODUCTS_EXAMPLE)
    query = st.text_input(label="What item are you looking for?", value=item, placeholder=item)
    clicked = st.form_submit_button('Submit')

# Run search when user enters a query
if clicked and query:
    st.write(query)
    with st.spinner(f"Searching for {query}..."):
        recommendations = recommender(query)
        st.write(recommendations)
    with st.spinner("Reviewing recommendations..."):
        reviews = reviewer(recommendations)
        st.write("**Review Summary:**")
        st.write(reviews)
