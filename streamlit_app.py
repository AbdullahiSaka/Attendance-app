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
st.title('Student Information and GPS Capture')

# JavaScript to prompt for location services
st.markdown("""
    <script>
        function getLocation() {
            if ("geolocation" in navigator) {
                navigator.geolocation.getCurrentPosition(function(position) {
                    Streamlit.setComponentValue(JSON.stringify({
                        latitude: position.coords.latitude,
                        longitude: position.coords.longitude
                    }));
                }, function(error) {
                    console.error('Error occurred: ', error);
                    Streamlit.setComponentValue(JSON.stringify({error: error.message}));
                }, {enableHighAccuracy: true, timeout: 10000, maximumAge: 0});
            } else {
                console.log("Geolocation is not supported by this browser.");
                Streamlit.setComponentValue(JSON.stringify({error: "Geolocation is not supported by this browser."}));
            }
        }

        // Trigger location request when the window loads
        window.onload = getLocation;
    </script>
""", unsafe_allow_html=True)

# Listen for location data or errors sent back from JavaScript
location_data = st.empty()

# Input fields for name and student ID, hidden until location is fetched
name = st.empty()
student_id = st.empty()
submit_button = st.empty()

# Use session_state to store whether location has been fetched to avoid re-fetching on reruns
if 'location_fetched' not in st.session_state:
    st.session_state['location_fetched'] = False

if st.session_state['location_fetched']:
    # Display input fields for name and student ID
    name = name.text_input('Enter your name', key='name')
    student_id = student_id.text_input('Enter your student ID', key='student_id')
    submit_button = submit_button.button('Submit')

# When the location is fetched or if there's an error
if st.experimental_get_query_params():
    location_json = st.experimental_get_query_params().get('data', [None])[0]
    if location_json:
        location = pd.json_normalize(json.loads(location_json))
        if 'error' not in location:
            st.session_state['location_fetched'] = True
            latitude = location['latitude'].values[0]
            longitude = location['longitude'].values[0]
            location_data.json({'Latitude': latitude, 'Longitude': longitude})
        else:
            location_data.error(location['error'].values[0])

if submit_button and name and student_id and 'latitude' in st.session_state and 'longitude' in st.session_state:
    # Save the data when the form is submitted
    save_data(name, student_id, st.session_state['latitude'], st.session_state['longitude'])
    st.success('Student data saved successfully!')
