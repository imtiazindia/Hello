import streamlit as st
import datetime

# Set page configuration
st.set_page_config(
    page_title="Hello World Live Deployment",
    page_icon="🌍",
    layout="centered"
)

# Main content
st.title("Hello World! 🌎")
st.write("This app is being deployed LIVE as we code!")

# Add some interactive elements
name = st.text_input("What's your name?")
if name:
    st.success(f"Hello, {name}! Welcome to your first Streamlit app! 🎉")

# Show current time
st.write(f"**Current time:** {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

# Add a fun button
if st.button("Celebrate!"):
    st.balloons()
    st.write("🎊 Congratulations! Your app is working! 🎊")

# Footer
st.markdown("---")
st.caption("Built live with ❤️ | Deployed on Streamlit Cloud")
