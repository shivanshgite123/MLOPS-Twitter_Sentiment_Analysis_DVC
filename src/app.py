import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image
import pickle
import re
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import nltk

# Download required NLTK data
nltk.download('punkt')
nltk.download('stopwords')

# Load the model and vectorizer
try:
    model = pickle.load(open('models/sentiment_model.pkl', 'rb'))
    vectorizer = pickle.load(open('models/vectorizer.pkl', 'rb'))
except:
    st.error("Error: Model files not found. Please ensure model files are present in the 'models' directory.")

def preprocess_text(text):
    # Convert to lowercase
    text = text.lower()
    
    # Remove special characters and numbers
    text = re.sub(r'[^a-zA-Z\s]', '', text)
    
    # Tokenization
    tokens = word_tokenize(text)
    
    # Remove stopwords
    stop_words = set(stopwords.words('english'))
    tokens = [token for token in tokens if token not in stop_words]
    
    # Join tokens back into text
    return ' '.join(tokens)

def predict_sentiment(text):
    # Preprocess the text
    processed_text = preprocess_text(text)
    
    # Vectorize the text
    text_vectorized = vectorizer.transform([processed_text])
    
    # Make prediction
    prediction = model.predict(text_vectorized)
    
    # Get probability scores
    proba = model.predict_proba(text_vectorized)
    
    return prediction[0], proba[0]

# Streamlit UI
def main():
    st.title("Twitter Sentiment Analysis")
    st.write("Analyze the sentiment of your text!")

    # Text input
    text_input = st.text_area("Enter your text here:", height=100)

    if st.button("Analyze Sentiment"):
        if text_input.strip() == "":
            st.warning("Please enter some text to analyze.")
        else:
            with st.spinner("Analyzing..."):
                # Get prediction and probability
                prediction, probability = predict_sentiment(text_input)
                
                # Display results
                st.subheader("Results:")
                
                # Create columns for better layout
                col1, col2 = st.columns(2)
                
                with col1:
                    st.write("Sentiment:")
                    if prediction == 1:
                        st.success("Positive 😊")
                    else:
                        st.error("Negative 😞")
                
                with col2:
                    st.write("Confidence:")
                    confidence = max(probability) * 100
                    st.progress(confidence/100)
                    st.write(f"{confidence:.2f}%")
                
                # Show preprocessed text
                st.subheader("Preprocessed Text:")
                st.write(preprocess_text(text_input))

    # Additional information
    with st.expander("About this app"):
        st.write("""
        This app uses a machine learning model trained on Twitter data to analyze sentiment.
        It classifies text as either positive or negative and provides a confidence score.
        The text preprocessing includes:
        - Converting to lowercase
        - Removing special characters and numbers
        - Removing stopwords
        - Tokenization
        """)

if __name__ == "__main__":
    main()