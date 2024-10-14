import streamlit as st
import requests
import json
from huggingface_hub import login

# Streamlit app title
st.title("vLLM Chatbot with Hugging Face Login")

# Hugging Face Login Section
if st.secrets:
    # Access the Hugging Face API token from secrets
    huggingface_api_token = st.secrets["api_keys"]["HUGGINGFACE_API_TOKEN"]

    if huggingface_api_token:
        try:
            # Log into Hugging Face using the API token
            login(token=huggingface_api_token)
            st.success("Successfully logged into Hugging Face!")
        except Exception as e:
            st.error(f"Login failed: {e}")
            st.stop()
    else:
        st.error("Hugging Face API token not found in secrets!")
        st.stop()
else:
    st.error("No secrets found!")
    st.stop()

# Define the vLLM server URL (adjust as needed if running remotely)
vllm_url = "http://localhost:8000/v1/chat/completions"

# User input prompt
user_input = st.text_input("Enter your prompt:")

# Function to send the request to the vLLM server
def get_vllm_response(prompt):
    headers = {"Content-Type": "application/json"}
    data = {
        "model": "meta-llama/Llama-3.2-1B",  # Model name served by vLLM
        "messages": [
            {"role": "user", "content": prompt}
        ]
    }
    
    # Send the request to the vLLM server
    response = requests.post(vllm_url, headers=headers, data=json.dumps(data))
    
    if response.status_code == 200:
        # Extract the generated text from the response
        result = response.json()
        return result["choices"][0]["message"]["content"]
    else:
        st.error(f"Error: {response.status_code} - {response.text}")
        return None

# Button to trigger the generation
if st.button("Generate"):
    if user_input:
        # Get the response from the vLLM server
        with st.spinner("Generating response..."):
            generated_text = get_vllm_response(user_input)

        if generated_text:
            st.write("Generated Response:", generated_text)
    else:
        st.warning("Please enter a prompt.")
