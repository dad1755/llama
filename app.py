import streamlit as st
from huggingface_hub import login
from transformers import pipeline

# Check if secrets are available
if st.secrets:
    st.write("Secrets exist!")

    # Access the Hugging Face API token from secrets
    huggingface_api_token = st.secrets["api_keys"]["HUGGINGFACE_API_TOKEN"]

    if huggingface_api_token:
        # Log into Hugging Face using the API token
        try:
            login(token=huggingface_api_token)
            st.success("Successfully logged into Hugging Face!")

            # Create the text generation pipeline
            pipe = pipeline("text-generation", model="meta-llama/Llama-3.2-1B")

            # User input
            user_input = st.text_input("Enter your prompt:")

            if st.button("Generate"):
                # Generate text
                if user_input:
                    generated_text = pipe(user_input, max_length=50, num_return_sequences=1)
                    st.write("Generated Text:", generated_text[0]['generated_text'])
                else:
                    st.warning("Please enter a prompt to generate text.")
        except Exception as e:
            st.error(f"Error logging in or creating the pipeline: {e}")
    else:
        st.error("Hugging Face token not found in secrets!")
else:
    st.write("No secrets found!")
