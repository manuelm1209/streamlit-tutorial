import streamlit as st
import time

#! This is for immutable files

@st.cache_data(ttl=60) #Cache the result of this function for 60 seconds
def fetch_data():
    #Simulate a data fetching operation
    time.sleep(3)
    return{"data": "fetched data"}

st.write("Fetching data...")
data = fetch_data()
st.write(data)