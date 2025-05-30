import streamlit as st

# KEEPS OBJECTS IN RAM

'''
1. Because resources are mutable, 
   and they hold live connections or open handles that shouldn’t be duplicated.
   
2. Using @st.cache_data for these could:
   -Create multiple connections
   -Lead to file-lock errors
   -Crash your app
   -Cause performance issues
   
3. Since resources like file handles can be sensitive:
   Always use .flush() to save the changes immediately.
   Don’t open the same file in multiple places without care.

'''

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

if st.button("Read File"):
    file_handler.seek(0)  # Move to the beginning
    content = file_handler.read()
    st.text(content)

# Button that calls the close_file function when clicked
st.button("Close File", on_click=file_handler.close)

#Cache data when you want to store pure data results.

Cache resource when you want to store live objects that are costly to recreate.

