import streamlit as st

# Streamlit app layout
st.title('Student Information and GPS Capture')

# Function to capture and display GPS location using JavaScript within the app
def show_location():
    st.write("""
        <div id="location">Waiting for location...</div>
        <script>
            navigator.geolocation.getCurrentPosition(function(position) {
                var lat = position.coords.latitude;
                var lon = position.coords.longitude;
                document.getElementById('location').innerHTML = 'Latitude: ' + lat + '<br>Longitude: ' + lon;
            }, function(error) {
                document.getElementById('location').innerHTML = 'Error getting location: ' + error.message;
            }, {enableHighAccuracy: true, timeout: 5000, maximumAge: 0});
        </script>
    """, unsafe_allow_html=True)

# Display location automatically
show_location()

# Form for student info
with st.form(key='student_info_form'):
    name = st.text_input(label='Enter your name')
    student_id = st.text_input(label='Enter your student ID')
    submit_button = st.form_submit_button(label='Submit')

if submit_button:
    # Here you can process the student's name and ID
    st.write(f"Name: {name}, Student ID: {student_id}")
