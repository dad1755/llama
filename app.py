import streamlit as st
from transformers import AutoTokenizer, AutoModelForCausalLM
import torch
from huggingface_hub import login

# Hugging Face Token login
login("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")

# Load tokenizer and model from Hugging Face
tokenizer = AutoTokenizer.from_pretrained("meta-llama/Llama-3.2-1B")
model = AutoModelForCausalLM.from_pretrained("meta-llama/Llama-3.2-1B")

# Streamlit user interface
st.title("LLama 3.2-1B Model Chatbot")

# Text input for the user prompt
user_input = st.text_input("Enter your prompt:")

if user_input:
    # Tokenize input and generate response
    inputs = tokenizer(user_input, return_tensors="pt")

    # Generate output from the model
    with torch.no_grad():
        outputs = model.generate(**inputs, max_length=100)

    # Decode the model's output tokens
    generated_text = tokenizer.decode(outputs[0], skip_special_tokens=True)

    # Display the generated text in Streamlit
    st.write(generated_text)
