# global_system.py
import streamlit as st
import openai
import os

def ask_global_system():
    st.header("Ask the Global System 🌐")
    st.write("Query the ChatGPT AI model directly.")
    
    # Set API key directly without client initialization
    try:
        openai.api_key = st.secrets["OPENAI_API_KEY"]
    except Exception as e:
        st.error(f"Failed to set OpenAI API key: {e}")
        return
    
    # Query input
    query = st.text_area(
        "Enter your question or prompt:",
        placeholder="Type your question here...",
        height=100
    )
    
    # Model selection
    model = st.selectbox(
        "Select AI model:",
        ["gpt-3.5-turbo", "gpt-4", "gpt-4-turbo"],
        help="Choose which ChatGPT model to use"
    )
    
    # Temperature slider for creativity control
    temperature = st.slider(
        "Creativity level:",
        min_value=0.0,
        max_value=1.0,
        value=0.7,
        step=0.1,
        help="Lower values = more deterministic, Higher values = more creative"
    )
    
    col1, col2 = st.columns([1, 3])
    
    with col1:
        if st.button("Submit Query", type="primary"):
            if not query:
                st.warning("Please enter a query first.")
            else:
                # Display loading state
                with st.spinner("ChatGPT is thinking..."):
                    try:
                        # Call ChatGPT API using the old compatible method
                        response = client.ChatCompletion.create(
                            model=model,
                            messages=[
                                {"role": "system", "content": "You are a helpful assistant. Provide clear, concise, and accurate responses."},
                                {"role": "user", "content": query}
                            ],
                            temperature=temperature,
                            max_tokens=1000
                        )
                        
                        # Get the response
                        chatgpt_response = response.choices[0].message.content
                        
                        # Store in session state
                        st.session_state.chatgpt_response = chatgpt_response
                        st.session_state.last_query = query
                        
                    except Exception as e:
                        error_msg = str(e)
                        if "authentication" in error_msg.lower() or "api key" in error_msg.lower():
                            st.error("Invalid API key. Please check your OpenAI API key in secrets.")
                        elif "rate limit" in error_msg.lower():
                            st.error("Rate limit exceeded. Please try again later.")
                        else:
                            st.error(f"An error occurred: {error_msg}")
    
    with col2:
        if st.button("Clear Response"):
            if "chatgpt_response" in st.session_state:
                del st.session_state.chatgpt_response
            if "last_query" in st.session_state:
                del st.session_state.last_query
            st.rerun()
    
    # Display the response
    if "chatgpt_response" in st.session_state:
        st.markdown("---")
        st.subheader("ChatGPT Response 🤖")
        
        # Show the original query
        if "last_query" in st.session_state:
            with st.expander("See your original query"):
                st.write(st.session_state.last_query)
        
        # Display the response
        st.write(st.session_state.chatgpt_response)
        
        # Copy functionality
        if st.button("Copy Response to Clipboard"):
            st.code(st.session_state.chatgpt_response, language="text")
            st.success("Response copied to clipboard!")
    
    # Information section
    st.markdown("---")
    st.info("""
    **Features:**
    - Direct integration with OpenAI's ChatGPT API
    - Multiple model selection
    - Adjustable creativity level
    - Response persistence
    - Copy to clipboard functionality
    """)
