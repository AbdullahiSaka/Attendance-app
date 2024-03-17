import streamlit as st
from bokeh.models.widgets import Button
from bokeh.models import CustomJS
from streamlit_bokeh_events import streamlit_bokeh_events
import pandas as pd
from datetime import datetime

# Function to save data (this is just a placeholder, adapt it to your needs)
def save_data(name, student_id, latitude, longitude):
    # Placeholder for saving data, e.g., append to a CSV or database
    st.success(f"Data saved: {name}, {student_id}, Lat: {latitude}, Lon: {longitude}")

# App title
st.title('MSc Students Attendance System')

# Input fields for name and student ID
name = st.text_input('Enter your name')
student_id = st.text_input('Enter your student ID')

# Bokeh button for getting location
loc_button = Button(label="Get Location", width=200)  # Adjust width as needed
loc_button.js_on_event("button_click", CustomJS(code="""
    navigator.geolocation.getCurrentPosition(
        (loc) => {
            document.dispatchEvent(new CustomEvent("GET_LOCATION", {detail: {lat: loc.coords.latitude, lon: loc.coords.longitude}}))
        }
    )
    """))

# Listen for the "GET_LOCATION" event and get the result
result = streamlit_bokeh_events(
    loc_button,
    events="GET_LOCATION",
    key="get_location",
    refresh_on_update=False,
    override_height=75,
    debounce_time=0)

# If the location is obtained, display it
if result:
    latitude = result["GET_LOCATION"]["lat"]
    longitude = result["GET_LOCATION"]["lon"]
    st.write(f"Latitude: {latitude}, Longitude: {longitude}")

    # When location is available, allow submission
    if st.button('Submit Attendance'):
        save_data(name, student_id, latitude, longitude)

# Additional logic for your app can go here
