import streamlit as st

# Check if secrets are empty or not
if st.secrets:
    st.write("Secrets exist!")
    # Optionally, display the available secrets (don't display sensitive data)
    st.write("Available secrets keys:", list(st.secrets.keys()))
else:
    st.write("No secrets found!")
