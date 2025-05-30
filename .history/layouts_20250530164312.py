
from datetime import datetime

# --- Sidebar Title and Description ---
st.sidebar.title("📚 Nihil's Smart Sidebar")
st.sidebar.markdown("Welcome! Use the tools below to interact with this app 🚀")

# --- User Input: Text Field ---
sidebar_input = st.sidebar.text_input("📝 Enter your name")

# --- User Input: Date Picker ---
selected_date = st.sidebar.date_input("📅 Select a date", value=datetime.today())

# --- User Input: Time Picker ---
selected_time = st.sidebar.time_input("⏰ Pick a time")

# --- User Input: Slider ---
satisfaction = st.sidebar.slider("😊 How satisfied are you?", min_value=0, max_value=10, value=5)

# --- Select Box: Category Selection ---
category = st.sidebar.selectbox(
    "📂 Choose a category",
    options=["General", "Education", "Technology", "Fun", "Feedback"]
)

# --- Checkbox for extra features ---
enable_advanced = st.sidebar.checkbox("🔧 Enable advanced options")

# --- Conditional rendering based on checkbox ---
if enable_advanced:
    st.sidebar.markdown("### 💡 Advanced Settings")
    volume = st.sidebar.slider("🔊 Volume Level", 0, 100, 50)
    brightness = st.sidebar.slider("💡 Brightness", 0, 100, 70)
    dark_mode = st.sidebar.toggle("🌙 Enable Dark Mode")

# --- Sidebar Button ---
if st.sidebar.button("🚀 Launch Now"):
    st.sidebar.success("Launched Successfully!")
    st.sidebar.balloons()

# --- Display summary inside the sidebar (or use in main area) ---
st.sidebar.markdown("---")
st.sidebar.markdown("### 🔍 Summary")
st.sidebar.write(f"👤 Name: {sidebar_input}")
st.sidebar.write(f"📆 Date: {selected_date}")
st.sidebar.write(f"⏰ Time: {selected_time}")
st.sidebar.write(f"😊 Satisfaction: {satisfaction}/10")
st.sidebar.write(f"📂 Category: {category}")
if enable_advanced:
    st.sidebar.write(f"🔊 Volume: {volume}")
    st.sidebar.write(f"💡 Brightness: {brightness}")
    st.sidebar.write(f"🌙 Dark Mode: {'On' if dark_mode else 'Off'}")
