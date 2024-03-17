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
st.title('Student Attendance System')

# Embed HTML and JavaScript for HTML5 Geolocation
st.markdown("""
    <div id="location"></div>
    <script>
        navigator.geolocation.getCurrentPosition(
            function(position) {
                var lat = position.coords.latitude;
                var lon = position.coords.longitude;
                document.getElementById('location').innerHTML =
                    'Latitude: ' + lat + '<br>Longitude: ' + lon;
            },
            function(error) {
                document.getElementById('location').innerHTML = 'Error: ' + error.message;
            },
            {enableHighAccuracy: true, timeout: 10000}
        );
    </script>
""", unsafe_allow_html=True)

# Input fields for name and student ID
name = st.text_input('Enter your name')
student_id = st.text_input('Enter your student ID')

# Manual input fields for latitude and longitude as a fallback
latitude_manual = st.text_input('Enter your Latitude (if automatic location failed)')
longitude_manual = st.text_input('Enter your Longitude (if automatic location failed)')

# Submit button
if st.button('Submit'):
    if name and student_id and (latitude_manual and longitude_manual):
        # Save the data when the form is submitted
        save_data(name, student_id, latitude_manual, longitude_manual)
        st.success('Student data saved successfully!')
    else:
        st.error('Please fill in all the fields.')
