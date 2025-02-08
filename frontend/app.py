import streamlit as st
import requests

st.set_page_config(page_title="AI Debate Assistant", layout="wide")

st.title("🎙️ AI Debate Assistant")
st.write("Enter a debate topic, and the AI will generate structured arguments for and against.")

# User Input
topic = st.text_input("Enter Debate Topic:")

if st.button("Generate Debate"):
    if topic:
        st.info("Generating arguments, please wait...")
        
        # Call FastAPI backend
        response = requests.post(
            "https://your-backend-url/generate-debate/",  # Change this after deploying FastAPI
            json={"topic": topic}
        )
        
        if response.status_code == 200:
            result = response.json()
            st.success("Debate Generated!")
            st.subheader(f"**Debate Topic:** {result['topic']}")
            st.markdown(result['arguments'])
        else:
            st.error("Failed to fetch debate arguments.")
    else:
        st.warning("Please enter a topic.")

