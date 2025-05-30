import streamlit as st

st.set_page_config(pa)

st.title("Home")


'''
When a Streamlit app is structured using a pages/ subfolder, and files like
1_page1.py, 2_page2.py, etc., are placed inside that folder, 
Streamlit automatically enables a sidebar-based multipage interface.
'''

# AS SOON AS THE PAGE IS RE-RENDERED, all of the state will be destroyed
# YOU NEED TO MANUALLY STORE IT IN st.session_state