import streamlit as st
from datetime import datetime

st.title("User Information Form")

form_values = {
    "name": None,
    "height": None,
    "gender": None,
    "dob": None,
}

# Importa datetime and add a min and max value to the st.date_input
min_date = datetime(1920,1,1)
max_date = datetime.now()

with st.form(key="User_info_form"):
    form_values["name"] = st.text_input("Enter your name: ")
    form_values["height"] = st.number_input("Enter your height (cm): ", step=1.00)
    form_values["gender"] = st.selectbox("Gender", ["Male", "Female"])
    form_values["dob"] = st.date_input("Enter your birthdate", min_value=min_date, max_value=max_date)
    
    submit_button = st.form_submit_button(label="Submit")
    if submit_button:
        if not all(form_values.values()):
            st.warning("Please fill in all of the fields")
        else:
            st.balloons()
            st.write("### Info")
            for (key, value) in form_values.items():
                st.write(f"{key.capitalize()}: {value}")