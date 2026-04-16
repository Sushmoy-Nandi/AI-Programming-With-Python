'''
Create an app that:
Takes a prompt from user
Sends it to Gemini API
Displays the generated response
'''

from google import genai
import os
from dotenv import load_dotenv
import streamlit as st

load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")
client = genai.Client(api_key=api_key)

st.title("Sushmoy AI Chat",anchor=False)

prompt = st.text_area("Enter your prompt", placeholder="Ask me anything...")

if st.button("Generate Response"):
    if not api_key:
        st.error("Please set GEMINI_API_KEY in your .env file.")
    elif not prompt.strip():
        st.warning("Please enter a prompt.")
    else:
        with st.spinner("Generating response..."):
            try:
                response = client.models.generate_content(
                    model="gemini-3-flash-preview",
                    contents=prompt
                )
                st.subheader("Response:",anchor=False)
                st.markdown(response.text)
            except Exception as e:
                st.error(f"Error: {e}")