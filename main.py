import os
from dotenv import load_dotenv
import streamlit as st
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import google.generativeai as genai

# Load API key
load_dotenv()
GEMINI_KEY = 'AIzaSyDnp6hmKk1OWSTdOtOnOugpPeQ1OhAS7aM'
genai.configure(api_key=GEMINI_KEY)
model = genai.GenerativeModel("gemini-1.5-flash")

docs = [
    'The mitochondria is the powerhouse of the cell.',
    'Georgia Tech is a leading research university in Atlanta.',
    'RAG combines document retrieval with language models for better factual accuracy.'
]

vectorizer = TfidfVectorizer()
doc_vectors = vectorizer.fit_transform(docs)

st.title("Simple RAG with Gemini")
user_query = st.text_input("Input your question:")

if user_query:
    query_vector = vectorizer.transform([user_query])
    sims = cosine_similarity(query_vector, doc_vectors).flatten()
    top_k = sims.argsort()[-2:][::-1]  # top 2 docs
    context = "\n".join([docs[i] for i in top_k])

    prompt = f"Given the following context as a baseline, answer the following question. You can add any previous knowledge about the subject, but use the provided context as the initial context:\n{context}\n\nQuestion: {user_query}"
    response = model.generate_content(prompt)

    st.markdown(f"**Context Used:**\n{context}")
    st.markdown("**Gemini Response:**")
    st.markdown(response.text)
