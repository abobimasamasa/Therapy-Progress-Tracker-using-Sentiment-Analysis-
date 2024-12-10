"""
Name: Ewa Stanley Chidozie 
Project: Therapy progress tracker application 
Purpose: Machine Learning Engineer Job Application 
company: Mentalync 
"""

import streamlit as st
from transformers import pipeline

# Load the sentiment analysis model
sentiment_model = pipeline("sentiment-analysis", model="distilbert-base-uncased-finetuned-sst-2-english")

# Function to analyze sentiment of input and return the sentiment label and score 
def calculate_sentiment(text):
    result = sentiment_model(text)
    return result[0]['label'], result[0]['score']

# Function to track progress based on GAD-7. PHQ-9 scores and session texts
def track_progress(gad7_scores, phq9_scores, session_texts):
    # Analyze sentiment of session texts
    sentiments = [calculate_sentiment(text) for text in session_texts]
    
    # structure results as a dictionary
    progress = {
        "sessions": [],
        "gad7_trend": gad7_scores,
        "phq9_trend": phq9_scores,
    }
    
    for i, (gad7, phq9, text, sentiment) in enumerate(zip(gad7_scores, phq9_scores, session_texts, sentiments)):
        progress["sessions"].append({
            "session_number": i + 1,
            "gad7_score": gad7,
            "phq9_score": phq9,
            "session_text": text,
            "sentiment_label": sentiment[0],
            "sentiment_score": sentiment[1],
        })

    return progress

# POC web interface Integration 
st.title("Therapy Progress Tracker")
st.write("Track progress between therapy sessions using GAD-7, PHQ-9 scores, and sentiment analysis.")

# Input for session 1
st.header("Client's Session 1")
gad7_session1 = st.slider("GAD-7 Score (Session 1)", 0, 21, 10)
phq9_session1 = st.slider("PHQ-9 Score (Session 1)", 0, 27, 12)
text_session1 = st.text_area("Session 1 Notes", "")

# Input for session 2
st.header("Client's Session 2")
gad7_session2 = st.slider("GAD-7 Score (Session 2)", 0, 21, 8)
phq9_session2 = st.slider("PHQ-9 Score (Session 2)", 0, 27, 10)
text_session2 = st.text_area("Session 2 Notes", "")

# Generate and display results
if st.button("Analyze Progress"):
    gad7_scores = [gad7_session1, gad7_session2]
    phq9_scores = [phq9_session1, phq9_session2]
    session_texts = [text_session1, text_session2]

    progress_report = track_progress(gad7_scores, phq9_scores, session_texts)

    st.subheader("Progress Report")
    for session in progress_report["sessions"]:
        st.markdown(f"### Session {session['session_number']}")
        st.write(f"GAD-7 Score: {session['gad7_score']}")
        st.write(f"PHQ-9 Score: {session['phq9_score']}")
        st.write(f"Sentiment: **{session['sentiment_label']}** ({session['sentiment_score']:.2f})")
        st.write(f"Notes: {session['session_text']}")
