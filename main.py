# main.py
import streamlit as st
from hello_module import hello_world, simple_hello

def main():
    """Main application entry point"""
    
    # Add a sidebar for navigation
    st.sidebar.title("Navigation")
    app_mode = st.sidebar.selectbox(
        "Choose the app mode",
        ["Full Hello World", "Simple Hello", "About"]
    )
    
    # Route to the appropriate function
    if app_mode == "Full Hello World":
        hello_world()
    elif app_mode == "Simple Hello":
        simple_hello()
    elif app_mode == "About":
        show_about()

def show_about():
    """About page"""
    st.title("About This App")
    st.write("""
    This is a modular Streamlit app demonstrating:
    - Separate module files
    - Function-based organization
    - Navigation between different views
    - Live deployment on Streamlit Cloud
    """)
    st.code("""
    Project Structure:
    hello-world-streamlit/
    ├── main.py          # Main entry point
    ├── hello_module.py  # Hello world functions
    └── requirements.txt # Dependencies
    """, language="bash")

if __name__ == "__main__":
    main()
