from google import genai
import os
from dotenv import load_dotenv
import os
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import streamlit as st
import pandas as pd



load_dotenv()

GEMINI_KEY = os.getenv("GEMINI_KEY")
client = genai.Client(api_key=GEMINI_KEY)

documents = []

for filename in os.listdir(".\documents"):
    if filename.endswith(".txt"):
        with open(os.path.join(".\documents", filename), "r", encoding="utf-8") as file:
            print(filename)
            documents.append(file.read())

vectorizer = TfidfVectorizer()

tfidf = vectorizer.fit_transform(documents)

ai_prompt = st.text_input("Enter your query here")
if ai_prompt:
    user_vector = vectorizer.transform([ai_prompt])
    sims = cosine_similarity(user_vector, tfidf).flatten()
    top_k = sims.argsort()[-2:][::-1]
    context = "\n".join([documents[i] for i in top_k])

    response = client.models.generate_content(model="gemini-2.0-flash", contents=[f"Given the following context as a baseline, answer the following question. You can add any previous knowledge about the subject, but use the provided context as the initial context. Context:\n{context}\n Question: {ai_prompt}"])
    print(f"Given the following context as a baseline, answer the following question. You can add any previous knowledge about the subject, but use the provided context as the initial context. Context:\n{context}\n Question: {ai_prompt}")
    ai_prompt = "<p style=font-size:40px;><b>" + ai_prompt + "</b></p>"
    st.markdown(ai_prompt, unsafe_allow_html=True)
    st.markdown(response.text)
    
