import streamlit as st

st.button("ok")
st.button("ok", key="btn2")

# min_value = st.slider("Set min value", 0, 50, 25)

# slider_value = st.slider("Slider", min_value, 100, min_value)

if "slider" not in st.session_state:
    st.session_state.slider = 25

min_value = st.slider("Set min value", 0, 50, 25)

st.session_state.slider = st.slider("Slider", min_value, 100, st.session_state.slider)
