import streamlit as st

if "step" not in st.session_state:
    st.session_state.step = 1
    
if "info" not in st.session_state:
    st.session_state.info = {}

# Callback funtions
def go_to_step2(name):
        print(f"{name}")
        st.session_state.step = 2
        
def go_to_step1():
    st.session_state.step = 1
    
    
if st.session_state.step == 1:
    st.header("Part 1: Info")
    
    name = st.text_input("Name", value=st.session_state.info.get("name", ""))
        
    if st.button("Next"):
        if not name:
            st.warning("Please fill in all of the fields")
        else:
            st.session_state.info["name"] = name
            st.session_state.step = 2

elif st.session_state.step == 2:
    st. header ("Part 2: Review")
    
    st.subheader("Please review this:")
    st.write(f"**Name**: {st.session_state.info.get('name','')}")
    
    if st.button("Submit"):
        st.success("Great!")
        st.balloons()
        st.session_state.info = {}
        
    st.button("Back", on_click=go_to_step1)
        