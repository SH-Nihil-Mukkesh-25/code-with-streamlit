import streamlit as st

# SIDEBAR LAYOUT

st.sidebar.title("This is a Sidebar")
st.sidebar.write("You can place elements like sliders, buttons, and text here")
sidebar_input = st.sidebar.text_input("Enter something in sidebar")

# TABS LAYOUT

tab1,tab2,tab3 = st.tabs(["Tab 1" , "Tab 2" , "Tab 3"])

# --- Tab 1 ---
with tab1:
    st.write("You are in Tab 1")
    st.text_input("Enter your name:")
    st.button("Click Me in Tab 1")

# --- Tab 2 ---
with tab2:
    st.write("You are in Tab 2")
    st.line_chart({"data": [3, 1, 4, 1, 5, 9]})
    st.selectbox("Choose a number:", [1, 2, 3, 4, 5])

# --- Tab 3 ---
with tab3:
    st.write("You are in Tab 3")
    st.checkbox("Enable Advanced Settings")
    st.slider("Adjust Value", min_value=0, max_value=100, value=50)
    
# COLUMNS LAYOUT

col1 , col2 = st.columns(2)

with col1 :
    st.header("Column 1")
    st.write("Content for column 1")
    
with col2 :
    st.header("Column 2")
    st.write("Content for column 2")
    
# Containers Example

with st.container(border=True):
    st.write("This is inside a container")
    st.write("You can think of containers as grouping of elements")
    st.write("Containers help manage sections of the page") 
    
# EMPTY PLACEHOLDER

placeholder = st.empty()   
placeholder.write("This is an empty placeholder, useful for dynamic content")

if st.button("Update PlaceHolder"):
    placeholder.write("The content of this placeholder has been updated")
    
with st.expander("Expand for more details"):
    st.write("This is additional information taht is hidden by default")
    

