import streamlit as st
import requests
import json

# Streamlit app title
st.title("vLLM Chatbot")

# Define the vLLM server URL
vllm_url = "http://localhost:8000/v1/chat/completions"

# User input prompt
user_input = st.text_input("Enter your prompt:")

# Function to send the request to the vLLM server
def get_vllm_response(prompt):
    headers = {"Content-Type": "application/json"}
    data = {
        "model": "meta-llama/Llama-3.2-1B",
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

# When the user presses the 'Generate' button
if st.button("Generate"):
    if user_input:
        # Get the response from the vLLM server
        with st.spinner("Generating response..."):
            generated_text = get_vllm_response(user_input)

        if generated_text:
            st.write("Generated Response:", generated_text)
    else:
        st.warning("Please enter a prompt.")
