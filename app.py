import streamlit as st
import requests
import json

# Set the API URL and authorization header
API_URL = "https://api-inference.huggingface.co/models/meta-llama/Llama-3.2-1B"
headers = {"Authorization": "Bearer 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"}

def query(payload):
    try:
        # Send a POST request to the API URL with the provided payload
        response = requests.post(API_URL, headers=headers, json=payload, timeout=10)
        
        # Check if the request was successful
        response.raise_for_status()
        return response.json()
    except requests.exceptions.HTTPError as http_err:
        st.error(f"HTTP error occurred: {http_err}")
    except requests.exceptions.ConnectionError as conn_err:
        st.error(f"Connection error occurred: {conn_err}")
    except requests.exceptions.Timeout as timeout_err:
        st.error(f"Request timed out: {timeout_err}")
    except requests.exceptions.RequestException as req_err:
        st.error(f"An error occurred: {req_err}")
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
            st.write(output)
        else:
            st.write("No response received.")
    else:
        st.error("Please enter a query before submitting.")
