import streamlit as st
from datetime import datetime

min_date = datetime(1920,1,1)
max_date = datetime.now()

st.title("User Information Form")

with st.form(key="user_info_form", clear_on_submit=True):
    name1 = st.text_input("Enter your firt name")
    
    birth_date = st.date_input("Enter your birth date", min_value=min_date, max_value=max_date)
    
    if birth_date:
        age = max_date.year - birth_date.year
        if birth_date.month > max_date.month or (birth_date.month == max_date.month and birth_date.day > max_date.day):
            age -= 1
        st.write(f"Your calculated age is {age} years")
        
    submit_button1 = st.form_submit_button(label="Submit Form")
    
    if submit_button1:
        if not name1 or not birth_date:
            st.warning("Please fill in all form inputs")
        else:
            st.success(f"Thank you, {name1}. Your age is {age}.")
            st.balloons()
            
    
    