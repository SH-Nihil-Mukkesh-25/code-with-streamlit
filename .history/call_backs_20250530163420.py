# Import the Streamlit library
import streamlit as st

# Check if "step" key exists in the session state; if not, initialize it to 1
# This controls which part of the form is being shown
if "step" not in st.session_state:
    st.session_state.step = 1

# Check if "info" key exists in the session state; if not, initialize it as an empty dictionary
# This will store user input across reruns
if "info" not in st.session_state:
    st.session_state.info = {}

# --- CALLBACK FUNCTION ---
# This function is triggered when the "Next" button is clicked
# It saves the name input and moves the form to step 2 (review step)
def go_to_step2(name):
    # Store the name in session_state
    st.session_state.info["name"] = name
    # Update the step to 2 to show the review screen
    st.session_state.step = 2

# Another callback function to go back to step 1
def go_to_step1():
    st.session_state.step = 1

# --- STEP 1: Info collection screen ---
# This block runs if the user is on step 1
if st.session_state.step == 1:
    st.header("Part 1: Info")

    # Get the name input from the user
    # The value is pre-filled from session state (if available), useful for going back and forth
    name = st.text_input("Name", value=st.session_state.info.get("name", ""))

    # Button to go to the next step
    # IMPORTANT: We use `on_click=go_to_step2` to call the function when the button is clicked
    # This callback ensures the step is changed during the same rerun
    # Without this, you'd need to click twice (once to set, once to see the effect)
    st.button("Next", on_click=go_to_step2, args=(name,))

# --- STEP 2: Review screen ---
# This block runs if the user is on step 2
if st.session_state.step == 2:
    st.header("Part 2: Review")

    # Ask the user to review what they've entered
    st.subheader("Please review this:")
    # Display the name retrieved from session state
    st.write(f"**Name**: {st.session_state.info.get('name', '')}")

    # When the user clicks submit:
    if st.button("Submit"):
        # Show success message
        st.success("Great!")
        # Display balloons animation
        st.balloons()
        # Clear stored info after submission (optional, for fresh restart)
        st.session_state.info = {}

    # Button to go back to step 1, using callback
    st.button("Back", on_click=go_to_step1)
