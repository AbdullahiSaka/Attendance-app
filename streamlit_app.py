import streamlit as st
import pandas as pd
from datetime import datetime
from streamlit_js_eval import get_geolocation

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
location = get_geolocation()

# Check if 'latitude' and 'longitude' are in the location dictionary
if location and 'latitude' in location and 'longitude' in location:
    latitude, longitude = location["latitude"], location["longitude"]
    st.write(f"Latitude: {latitude}, Longitude: {longitude}")
else:
    st.error("Failed to retrieve your location. Please ensure location services are enabled and try again, or manually enter your location.")

# Input fields for name and student ID, and manual location entry as a fallback
name = st.text_input('Enter your name')
student_id = st.text_input('Enter your student ID')
latitude_manual = st.text_input('Enter your Latitude (if automatic location failed)')
longitude_manual = st.text_input('Enter your Longitude (if automatic location failed)')

# Use automatic location if available, otherwise fall back to manual entry
latitude = latitude if 'latitude' in locals() else latitude_manual
longitude = longitude if 'longitude' in locals() else longitude_manual

if st.button('Submit') and name and student_id and latitude and longitude:
    save_data(name, student_id, latitude, longitude)
    st.success('Student data saved successfully!')
else:
    st.error('Please fill in all the fields and ensure you have either provided location access or entered your location manually.')
