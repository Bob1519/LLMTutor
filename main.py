from google import genai
import os
from dotenv import load_dotenv

import streamlit as st

load_dotenv()


GEMINI_KEY = os.getenv("GEMINI_KEY")

client = genai.Client(api_key=GEMINI_KEY)

# 4. Streamlit UI
ai_prompt = st.text_input("Input your question:")
if ai_prompt:
    response = client.models.generate_content(
        model="gemini-2.0-flash",
        contents=[ai_prompt]
    )
    # Display prompt and AI answer
    styled_prompt = f"<p style='font-size:40px;'><b>{ai_prompt}</b></p>"
    st.markdown(styled_prompt, unsafe_allow_html=True)
    st.markdown(response.text)
