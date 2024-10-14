import streamlit as st
from transformers import pipeline

# Check if secrets are available
if st.secrets:
    st.write("Secrets exist!")
    st.write("Available secrets keys:", list(st.secrets.keys()))

    # Access the REPLICATE_API_TOKEN from secrets
    replicate_api_token = st.secrets["REPLICATE_API_TOKEN"]
    
    # Use the token to authenticate the pipeline
    try:
        # Set the token in the environment (needed for Hugging Face authentication)
        import os
        os.environ["HUGGINGFACEHUB_API_TOKEN"] = replicate_api_token
        
        # Create the text generation pipeline
        pipe = pipeline("text-generation", model="meta-llama/Llama-3.2-1B")
        
        # Input from user
        user_input = st.text_input("Enter your prompt:")

        if st.button("Generate"):
            # Generate text
            if user_input:
                generated_text = pipe(user_input, max_length=50, num_return_sequences=1)
                st.write("Generated Text:", generated_text[0]['generated_text'])
            else:
                st.warning("Please enter a prompt to generate text.")
    except Exception as e:
        st.error(f"Error creating the pipeline: {e}")
else:
    st.write("No secrets found!")
