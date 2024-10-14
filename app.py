import requests

# Set the API URL and authorization header
API_URL = "https://api-inference.huggingface.co/models/meta-llama/Llama-3.2-1B"
headers = {"Authorization": "Bearer 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"}

def query(payload):
    # Send a POST request to the API URL with the provided payload
    response = requests.post(API_URL, headers=headers, json=payload)
    
    # Check if the request was successful
    if response.status_code == 200:
        return response.json()
    else:
        # Handle errors
        print(f"Error: {response.status_code}, {response.text}")
        return None

# Example query payload
output = query({
    "inputs": "Can you please let us know more details about your "
})

# Output the response from the model
if output:
    print("Response from model:")
    print(output)
