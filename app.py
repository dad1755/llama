import streamlit as st

# Check if secrets are available
if st.secrets:
    st.write("Secrets exist!")
    st.write("Available secrets keys:", list(st.secrets.keys()))

    # Access the REPLICATE_API_TOKEN from secrets
    replicate_api_token = st.secrets["REPLICATE_API_TOKEN"]
    
    # Display or use the token (be careful with sensitive data)
    st.write("Replicate API Token:", replicate_api_token)
else:
    st.write("No secrets found!")
