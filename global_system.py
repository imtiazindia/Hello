# global_system.py
import streamlit as st

def ask_global_system():
    st.header("Ask the Global System 🌐")
    st.write("This is the global system query interface.")
    
    # Add your global system functionality here
    query = st.text_area("Enter your query for the global AI system:")
    
    if st.button("Submit Query"):
        if query:
            st.success(f"Query submitted to global system: {query}")
            # Add your global system processing logic here
        else:
            st.warning("Please enter a query first.")
    
    st.info("Global system allows you to query the central AI model directly.")
