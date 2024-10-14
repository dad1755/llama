import streamlit as st
import requests
import time

# Set the API URL and authorization header
API_URL = "https://api-inference.huggingface.co/models/meta-llama/Llama-3.2-1B"
headers = {"Authorization": "Bearer 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"}

def query(payload, retries=3):
    for i in range(retries):
        try:
            response = requests.post(API_URL, headers=headers, json=payload, timeout=30)
            response.raise_for_status()  # Raise an error for HTTP errors
            return response.json()
        except requests.exceptions.HTTPError as http_err:
            st.error(f"HTTP error occurred: {http_err}")
            return None
        except requests.exceptions.ConnectionError as conn_err:
            st.error(f"Connection error occurred: {conn_err}")
            return None
        except requests.exceptions.Timeout as timeout_err:
            st.warning(f"Request timed out: {timeout_err}. Retrying {retries - i - 1} more times...")
            time.sleep(5)  # Wait for 5 seconds before retrying
        except requests.exceptions.RequestException as req_err:
            st.error(f"An error occurred: {req_err}")
            return None
    return None

# Streamlit user interface
st.title("Hugging Face API Query")

# Input box for user query
user_input = st.text_input("Enter your query:", "")

if st.button("Submit"):
    if user_input:
        with st.spinner("Generating response..."):
            output = query({"inputs": user_input})
        
        # Display the response
        if output:
            st.subheader("Response from Model:")
            # Extract the generated text
            generated_text = output[0].get("generated_text", "No text generated.")
            # Display the generated text
            st.markdown(generated_text)  # Use st.markdown for better formatting
        else:
            st.write("No response received.")
    else:
        st.error("Please enter a query before submitting.")
