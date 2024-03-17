import streamlit as st
import pandas as pd
from datetime import datetime

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
st.title('MSc Student Attendance System')

# Input fields for name and student ID
name = st.text_input('Enter your name', key='name')
student_id = st.text_input('Enter your student ID', key='student_id')

# JavaScript to capture GPS location and trigger form submission
st.markdown("""
    <script>
        function getLocation() {
            if (navigator.geolocation) {
                navigator.geolocation.getCurrentPosition(showPosition);
            } else { 
                console.log("Geolocation is not supported by this browser.");
            }
        }

        function showPosition(position) {
            document.getElementById('latitude').value = position.coords.latitude;
            document.getElementById('longitude').value = position.coords.longitude;
            document.getElementById('hidden_submit').click(); // Trigger form submission
        }

        window.onload = getLocation; // Trigger location capture on page load
    </script>
    <input type='text' id='latitude' hidden>
    <input type='text' id='longitude' hidden>
""", unsafe_allow_html=True)

# Hidden form to submit GPS coordinates
if st.button('Click to submit your information', key='hidden_submit'):
    # Using the st.session_state to access values set by JavaScript
    latitude = st.session_state.get('latitude', '')
    longitude = st.session_state.get('longitude', '')

    if name and student_id and latitude and longitude:
        save_data(name, student_id, latitude, longitude)
        st.success('Student data saved successfully!')
    else:
        st.error('Failed to capture GPS coordinates. Please ensure your location services are enabled and try again.')
