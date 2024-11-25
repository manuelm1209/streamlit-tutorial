import streamlit as st 
import os

st.title("Super APP")
st.header("Header")
st.subheader("Subheader")
st.markdown("This is **Markdown** _italics_")
st.caption("Caption")

# Adding code blocks
code_example = """
def greet(name):
    print('hello', name)
"""
st.code(code_example, language="python")

st.divider()

# Adding images
st.image(os.path.join(os.getcwd(), "static", "image.png"))
"Second image"
st.image(os.path.join(os.getcwd(), "static", "image.png"), width=100)