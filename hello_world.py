import streamlit as st
import datetime
import time

# Set page configuration - FIXED THE TYPO
st.set_page_config(
    page_title="Hello World Live Deployment",
    page_icon="🌍",  # Changed from page_-icon to page_icon
    layout="centered"
)

# Main content
st.title("Hello World! 🌎")
st.write("This app is being deployed LIVE as we code!")

# Add some interactive elements
name = st.text_input("What's your name?")
if name:
    st.success(f"Hello, {name}! Welcome to your first Streamlit app! 🎉")

# Show current time with auto-refresh
st.write(f"**Current time:** {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
st.caption("This updates automatically when the app refreshes")

# Add a fun button
if st.button("Celebrate!"):
    st.balloons()
    st.write("🎊 Congratulations! Your app is working! 🎊")

# Add a slider for fun
number = st.slider("Pick a number between 1-10", 1, 10)
st.write(f"You selected: {'⭐' * number}")

# Progress bar example
if st.button("Show progress"):
    progress_bar = st.progress(0)
    for i in range(100):
        time.sleep(0.01)
        progress_bar.progress(i + 1)
    st.write("Progress complete! ✅")

# Footer
st.markdown("---")
st.caption("Built live with ❤️ | Deployed on Streamlit Cloud | Auto-updates on save")
