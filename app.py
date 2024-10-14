import requests
import json

# Set the API URL and authorization header
API_URL = "https://api-inference.huggingface.co/models/meta-llama/Llama-3.2-1B"
headers = {"Authorization": "Bearer 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"}

def query(payload):
    try:
        # Send a POST request to the API URL with the provided payload
        response = requests.post(API_URL, headers=headers, json=payload, timeout=10)  # Added timeout
        
        # Check if the request was successful
        response.raise_for_status()  # This will raise an error for HTTP errors
        return response.json()
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")  # Log HTTP errors
    except requests.exceptions.ConnectionError as conn_err:
        print(f"Connection error occurred: {conn_err}")  # Log connection errors
    except requests.exceptions.Timeout as timeout_err:
        print(f"Request timed out: {timeout_err}")  # Log timeout errors
    except requests.exceptions.RequestException as req_err:
        print(f"An error occurred: {req_err}")  # Log any other request errors
    return None

# Example query payload
output = query({
    "inputs": "Can you please let us know more details about your "
})

# Output the response from the model
if output:
    print("Response from model:")
    print(output)
else:
    print("No response received.")
