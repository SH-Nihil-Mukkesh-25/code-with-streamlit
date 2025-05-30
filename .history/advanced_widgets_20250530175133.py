import streamlit as st

# Each widget has an unique key/id automatically generated.
# If 2 widgets are same, they'll throw a StreamlitDuplicateElementId Error

st.button("Ok")
st.button("Ok",key="btn2") # NOW THEY DONT GIVE ANY ERRORS

# key = "btn2" refers to a unique identifier used to access values in an object

if "slider" not in st.session_state:
    st.session_state.slider = 25

min_value = st.slider("Set min value",0,50,25)
slider_value = st.slider("Slider",min_value,100,min_value)
st.session_state.slider = st.slider("Slider",min_value,100,st.session_state.slider)

# If you want a slider that keeps its value between interactions 
# and depends on the first slider's minimum, use the third approach with st.session_state.

