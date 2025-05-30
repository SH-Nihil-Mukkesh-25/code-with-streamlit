import streamlit as st
import os

st.write("Hello World")

# Any time something must be updated on the screen,Streamlit reruns your entire Script from TOP to BOTTOM

pressed = st.button("Press Me")
print(pressed)

# By default it is in 'false', when you press it becomes 'true'
# in Streamlit, pressing a button causes the entire script to rerun from the top.
# When a Streamlit script reruns, the button state resets to 'false'

st.divider()

# TEXT FORMATS

st.title("Super Simple Title")
st.header("This is a Header")
st.subheader("Subheader")
st.markdown("This is a **MarkDown**") # bold
st.markdown("This is a _MarkDown_") # italic
st.caption("Small Text")

code_example = """
public void codeExample {
    System.out.println("Hello");
}
"""

st.code(code_example , language="java")

st.divider()

# Image

st.image(os.path.join(os.getcwd(),"YUCI hiring.jpg") , width=100 ) 