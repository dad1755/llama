import streamlit as st
from huggingface_hub import login
from transformers import AutoTokenizer, AutoModelForCausalLM
import torch

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
        except Exception as e:
            st.error(f"Login failed: {e}")
            st.stop()

        # Try to load the model and tokenizer directly
        try:
            st.write("Loading model and tokenizer...")

            # Load the tokenizer and model directly
            tokenizer = AutoTokenizer.from_pretrained("meta-llama/Llama-3.2-1B")
            model = AutoModelForCausalLM.from_pretrained("meta-llama/Llama-3.2-1B")

            st.success("Model and tokenizer successfully loaded!")

            # User input
            user_input = st.text_input("Enter your prompt:")

            if st.button("Generate"):
                if user_input:
                    # Tokenize the input
                    inputs = tokenizer(user_input, return_tensors="pt")

                    # Generate text (using a small max_length to prevent resource issues)
                    with st.spinner("Generating text..."):
                        outputs = model.generate(inputs["input_ids"], max_length=50)

                    # Decode and display the generated text
                    generated_text = tokenizer.decode(outputs[0], skip_special_tokens=True)
                    st.write("Generated Text:", generated_text)
                else:
                    st.warning("Please enter a prompt to generate text.")
        except Exception as e:
            st.error(f"Error loading the model or generating text: {e}")
else:
    st.write("No secrets found!")
