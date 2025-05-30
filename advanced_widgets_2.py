import streamlit as st

# Initialize user_input in session_state if not present
if "user_input" not in st.session_state:
    st.session_state.user_input = ""

# Checkbox to show/hide input field
show_input = st.checkbox("Show Input Field")

# Show input box only if checkbox is checked
if show_input:
    user_input = st.text_input("Enter something:", value=st.session_state.user_input)
    st.session_state.user_input = user_input

# Display the current user input
st.write(f"User Input: {st.session_state.user_input}")

# 1. st.session_state
#    - A special dictionary-like object that stores variables persistently across reruns of the Streamlit app.
#    - Streamlit reruns the whole script each time the user interacts (e.g., clicks a checkbox),
#      so without session_state, variables would reset every time.
#    - Here, we initialize user_input in session_state if it doesn’t exist, so we can remember what the user typed before.
#
# 2. Checkbox Widget (st.checkbox)
#    - Creates a checkbox UI element that returns True if checked, else False.
#    - We assign the returned value to show_input to control whether to show the input box.
#
# 3. Text Input Widget (st.text_input)
#    - Displays a text box where users can type input.
#    - The value parameter sets the initial/default text inside the box.
#    - We use the saved user_input from session state as the default so the input box shows the last entered text when visible.
#
# 4. Saving Input in Session State
#    - When the user types in the text box, we immediately save the new value back to st.session_state.user_input.
#    - This ensures that even if the input box is hidden (checkbox unchecked), the last input is retained and displayed.
#
# 5. Displaying User Input
#    - The final st.write command shows the current value of user_input stored in session state,
#      so users can always see their input even if the text box is hidden.
