import streamlit as st
import pandas as pd
from datetime import datetime
from streamlit_js_eval import streamlit_js_eval, get_geolocation

# Function to save data to a CSV file
def save_data(name, student_id, latitude, longitude):
    new_data = pd.DataFrame({
        'Name': [name],
        'Student ID': [student_id],
        'Latitude': [latitude],
        'Longitude': [longitude],
        'Timestamp': [datetime.now()]
    })
    try:
        data = pd.read_csv('student_data.csv')
        data = pd.concat([data, new_data], ignore_index=True)
    except FileNotFoundError:
        data = new_data
    data.to_csv('student_data.csv', index=False)

# Streamlit app layout
st.title('Student Information and GPS Capture')

# Attempt to get geolocation
location = get_geolocation(timeout=5000)

if location:
    latitude, longitude = location["latitude"], location["longitude"]
    st.write(f"Latitude: {latitude}, Longitude: {longitude}")
else:
    st.error("Failed to retrieve your location. Please ensure location services are enabled and try again.")

# Input fields for name and student ID
name = st.text_input('Enter your name')
student_id = st.text_input('Enter your student ID')

if st.button('Submit') and name and student_id and location:
    save_data(name, student_id, latitude, longitude)
    st.success('Student data saved successfully!')
else:
    st.error('Please fill in all the fields.')
