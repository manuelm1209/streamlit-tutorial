import streamlit as st

# Sidebar layout
st.sidebar.title("This is the sidebar")
st.sidebar.write("Text in the sidebar")
sidebar_input = st.sidebar.text_input("Enter something in the sidebar")

# Tabs layout
tab1, tab2, tab3 = st.tabs(["Tab 1", "Tab 2", "Tab 3"])

with tab1:
    st.write("You are in Tab 1")
    
with tab2:
    st.write("You are in Tab 2")
    
with tab3:
    st.write("You are in Tab 3")
    
# Columns layout
col1, col2 = st.columns(2)
with col1:
    st.header("Column 1")
    st.write("Content for column 1")
    
with col2:
    st.header("Column 2")
    st.write("Content for column 2")
    
col3, col4, col5 = st.columns([2,1,1])
with col3:
    st.header("Column 3")
    st.write("Content for column 3")
    
with col4:
    st.header("Column 4")
    st.write("Content for column 4")
    
with col5:
    st.header("Column 5")
    st.write("Content for column 5")

# Containers example
with st.container (border=True):
    st.write("This is inside a container.")
    st.write("You can think of containers a grouping for elements.")
    st.write("Containers help manage sections of the.")
# Without border
with st.container (border=False):
    st.write("This is inside a container.")
    st.write("You can think of containers a grouping for elements.")
    st.write("Containers help manage sections of the.")
    
st.divider()

# Empty placehorder (Dynamic)
placeholder = st.empty()
placeholder.write("Initial")

if st.button("Update Placeholder"):
    placeholder.write("Updated Content")
    
# Expander
with st.expander("Expand for more details", icon="🔥"):
    st.write("This is inside a container.")
    st.write("You can think of containers a grouping for elements.")
    st.write("Containers help manage sections of the.")
    
# Tooltip (Popover)
st.caption("Hover over this button for a tooltip")
st.button("Button with Tooltip", help="This is a tooltip or popover on hover")

# Sidebar input handling
if sidebar_input:
    st.markdown(f"### You entered in the sidebar: {sidebar_input}")