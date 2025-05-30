import streamlit as st



file_path = "example.txt"

# ✅ Cache the file handler as a resource (not data)
@st.cache_resource
def get_file_handler():
    # Open the file in append mode (creates if it doesn't exist)
    file = open(file_path, "a")
    return file

# 📦 Get the cached file handler
file_handler = get_file_handler()

# 📝 Write to the file when button is clicked
if st.button("Write to File"):
    file_handler.write("New line of text\n")
    file_handler.flush()  # Ensures it's written immediately
    st.success("Wrote a new line to the file!")
