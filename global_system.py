# global_system.py
import streamlit as st
import httpx
from openai import OpenAI

def ask_global_system():
    st.header("Ask the Global System 🌐")
    st.write("Query the ChatGPT AI model directly.")
    
    # Debug: Check secret access
    try:
        key = st.secrets["OPENAI_API_KEY"]
        st.sidebar.success(f"✅ API key found: {key[:12]}...")
    except:
        st.sidebar.error("❌ OPENAI_API_KEY not found in secrets")
        st.error("Please add OPENAI_API_KEY to your Streamlit Cloud secrets")
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
                        # Create custom HTTP client to bypass Streamlit's proxy injection
                        http_client = httpx.Client()
                        
                        # Initialize OpenAI client with explicit HTTP client
                        client = OpenAI(
                            api_key=st.secrets["OPENAI_API_KEY"],
                            http_client=http_client
                        )
                        
                        # Test with a very simple call first
                        response = client.chat.completions.create(
                            model="gpt-3.5-turbo",  # Use most reliable model
                            messages=[
                                {"role": "user", "content": "Hello"}  # Simple test message
                            ],
                            max_tokens=10
                        )
                        
                        # If simple test works, proceed with actual query
                        response = client.chat.completions.create(
                            model=model,
                            messages=[
                                {"role": "system", "content": "You are a helpful assistant. Provide clear, concise, and accurate responses."},
                                {"role": "user", "content": query}
                            ],
                            temperature=temperature,
                            max_tokens=1000
                        )
                        
                        chatgpt_response = response.choices[0].message.content
                        
                        # Store in session state
                        st.session_state.chatgpt_response = chatgpt_response
                        st.session_state.last_query = query
                        
                        # Close the HTTP client
                        http_client.close()
                        
                    except Exception as e:
                        # More specific error handling
                        error_msg = str(e)
                        if "401" in error_msg or "authentication" in error_msg.lower():
                            st.error("""
                            **Authentication Failed!**
                            
                            Please check:
                            1. 🔑 API key is correct in Streamlit Cloud secrets
                            2. 📋 Key is copied exactly (no extra spaces)
                            3. ⏰ Key is not expired
                            4. 🌐 You have API access in your OpenAI account
                            
                            **To fix:** Go to Streamlit Cloud → App Settings → Secrets → Update OPENAI_API_KEY
                            """)
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
