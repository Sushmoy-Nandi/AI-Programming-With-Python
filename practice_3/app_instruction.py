'''
Build an app that:
Takes a sentence from user
Sends to Gemini with instruction:
 “Improve this sentence professionally”
Displays improved version
Example:
 Input: "i want job"
 Output: "I am seeking a professional opportunity."

'''

from google import genai
import os
from dotenv import load_dotenv
import streamlit as st

load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")
client = genai.Client(api_key=api_key)

st.title("Professional Sentence Improver",anchor=False)
st.write("Enter a sentence and Gemini will rewrite it professionally.")

sentence = st.text_area("Enter your sentence", placeholder='e.g. "i want job"')

if st.button("Improve Sentence"):
    if not api_key:
        st.error("Please set GEMINI_API_KEY in your .env file.")
    elif not sentence.strip():
        st.warning("Please enter a sentence.")
    else:
        with st.spinner("Improving your sentence..."):
            try:
                prompt = f'Improve this sentence professionally: "{sentence.strip()}"'
                response = client.models.generate_content(
                    model="gemini-3-flash-preview",
                    contents=prompt
                )
                st.subheader("Improved Sentence:",anchor=False)
                st.success(response.text.strip())
            except Exception as e:
                st.error(f"Error: {e}")