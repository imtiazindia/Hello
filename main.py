# main.py
import streamlit as st
from global_system import ask_global_system
from folder_feeder import feed_folder
from file_feeder import feed_files

# Set page configuration
st.set_page_config(
    page_title="AI Model Feeder",
    page_icon="🤖",
    layout="wide"
)

def main():
    """Main application entry point"""
    
    # Sidebar navigation
    st.sidebar.title("AI Model Feeder 🤖")
   
    # Second selectbox - feeding method
    feed_method = st.sidebar.selectbox(
        "How do you want to feed the AI model",
        ["Ask the global system", "Feed a folder", "Feed files"]
    )
    
    # Main content area based on feeding method selection
    if feed_method == "Ask the global system":
        ask_global_system()
        
    elif feed_method == "Feed a folder":
        feed_folder()
        
    elif feed_method == "Feed files":
        feed_files()
    
    # You can keep your original app mode logic here if needed
    #if app_mode == "About":
    #    show_about()

def show_about():
    """About page"""
    st.sidebar.markdown("---")
    st.sidebar.info("""
    This app demonstrates different ways to feed data to an AI model:
    - Global System: Direct queries
    - Folder Feeding: Batch processing
    - File Feeding: Individual document processing
    """)

if __name__ == "__main__":
    main()
