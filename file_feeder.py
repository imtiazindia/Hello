# file_feeder.py
import streamlit as st

def feed_files():
    st.header("Feed Files 📄")
    st.write("Upload individual files for processing.")
    
    # Add your file feeding functionality here
    uploaded_files = st.file_uploader(
        "Choose files to process",
        type=['txt', 'pdf', 'docx', 'csv', 'json'],
        accept_multiple_files=True,
        help="Select one or more files to feed to the AI model"
    )
    
    if uploaded_files:
        st.success(f"Uploaded {len(uploaded_files)} file(s)")
        
        # File processing options
        process_option = st.radio(
            "Processing option:",
            ["Process all files together", "Process files individually"]
        )
        
        if st.button("Process Files"):
            st.write(f"Processing {len(uploaded_files)} files with option: {process_option}")
            # Add your file processing logic here
    
    st.info("File feeding allows individual document processing with custom options.")
