# hello_module.py
import streamlit as st
import datetime
import time

def hello_world():
    """Main hello world function with all the components"""
    
    # REMOVED st.set_page_config() from here
    
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

def simple_hello():
    """Simple hello function for quick testing"""
    st.title("Simple Hello! 👋")
    st.write("This is the simple version from the module!")
    st.info("Module import is working correctly!")
