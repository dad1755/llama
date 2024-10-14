import streamlit as st
from huggingface_hub import InferenceClient

# Retrieve the API key from Streamlit secrets
api_key = st.secrets["api_keys"]["REPLICATE_API_TOKEN"]

# Initialize the InferenceClient with the API key
client = InferenceClient(api_key=api_key)

# Image URL to be processed
image_url = "https://cdn.britannica.com/61/93061-050-99147DCE/Statue-of-Liberty-Island-New-York-Bay.jpg"

# User prompt for image description
user_prompt = "Describe this image in one sentence."

# Prepare messages for chat completion
messages = [
    {
        "role": "user",
        "content": [
            {"type": "image_url", "image_url": {"url": image_url}},
            {"type": "text", "text": user_prompt},
        ],
    }
]

# Use the chat_completion method to get responses from the model
st.title("Image Description Using LLaMA 3.2")
st.subheader("Image URL:")
st.image(image_url)

if st.button("Describe Image"):
    with st.spinner("Generating description..."):
        # Call the model and stream responses
        for message in client.chat_completion(
            model="meta-llama/Llama-3.2-11B-Vision-Instruct",
            messages=messages,
            max_tokens=500,
            stream=True,
        ):
            # Print the generated description
            st.write(message.choices[0].delta.content, end="")
