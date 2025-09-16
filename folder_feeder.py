# folder_feeder.py
import streamlit as st

def feed_folder():
    st.header("Feed a Folder 📁")
    st.write("Upload or select a folder to process.")
    
    # Add your folder feeding functionality here
    uploaded_folder = st.file_uploader(
        "Choose a folder (or multiple files)",
        type=None,
        accept_multiple_files=True,
        help="Select multiple files or a zip file containing your documents"
    )
    
    if uploaded_folder:
        st.success(f"Selected {len(uploaded_folder)} files for processing")
        # Add your folder processing logic here
        
        # Show file details
        for i, file in enumerate(uploaded_folder):
            st.write(f"File {i+1}: {file.name} ({len(file.getvalue())} bytes)")
    
    st.info("Folder feeding processes multiple documents at once for batch analysis.")
