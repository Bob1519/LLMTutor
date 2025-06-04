from google import genai
import os
from dotenv import load_dotenv

import streamlit as st
import pandas as pd



load_dotenv()

GEMINI_KEY = os.getenv("GEMINI_KEY")
client = genai.Client(api_key=GEMINI_KEY)

ai_prompt = st.text_input("Enter your query here")
if ai_prompt:
    response = client.models.generate_content(model="gemini-2.0-flash", contents=[ai_prompt])
    ai_prompt = "<p style=font-size:40px;><b>" + ai_prompt + "</b></p>"
    st.markdown(ai_prompt, unsafe_allow_html=True)
    st.markdown(response.text)
    
