import streamlit as st

if "checkbox" not in st.session_state:
    st.session_state.checkbox = False

def toggle_input():
    st.session_state.checkbox = not st.session_state.checkbox
        
st.checkbox("Show Input Field", value=st.session_state.checkbox, on_change=toggle_input)

# if "user_input" not in st.session_state:
#     st.session_state.user_input = ""

# st.session_state.checkbox = bool(st.session_state.get("checkbox", False))

if st.session_state.checkbox:
    user_input = st.text_input("Enter something:", value=st.session_state.user_input)
    st.session_state.user_input = user_input
else:
    user_input = st.session_state.get("user_input", "")
    
st.write(f"User Input: {user_input}")
