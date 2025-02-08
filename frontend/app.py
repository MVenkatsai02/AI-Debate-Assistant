import streamlit as st
import requests

# Set Streamlit page configuration
st.set_page_config(page_title="AI Debate Assistant", layout="wide")

# App Title
st.title("🎙️ AI Debate Assistant")
st.write("Enter a debate topic, and the AI will generate structured arguments for and against.")

# User Input for Debate Topic
topic = st.text_input("Enter Debate Topic:")

# Backend API URL (Updated with Render deployment)
API_URL = "https://ai-debate-assistant.onrender.com/generate-debate/"

if st.button("Generate Debate"):
    if topic:
        st.info("Generating arguments, please wait...")
        
        try:
            # Call FastAPI backend on Render
            response = requests.post(API_URL, json={"topic": topic})

            if response.status_code == 200:
                result = response.json()
                st.success("Debate Generated!")
                st.subheader(f"**Debate Topic:** {result['topic']}")
                st.markdown(result['arguments'])
            else:
                st.error(f"Failed to fetch debate arguments. Error Code: {response.status_code}")
        except requests.exceptions.RequestException as e:
            st.error(f"Request failed: {e}")
    else:
        st.warning("Please enter a topic.")
