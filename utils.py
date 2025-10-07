import streamlit as st
import google.generativeai as genai
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

def configure_gemini():
    """Configure Gemini API"""
    api_key = os.getenv('GEMINI_API_KEY')
    if not api_key:
        st.error("Please set GEMINI_API_KEY in your .env file")
        st.stop()
    
    genai.configure(api_key=api_key)
    return genai.GenerativeModel('models/gemini-2.5-pro')  # or 'models/gemini-2.5-flash'

def generate_response(prompt, context=""):
    """Generate response using Gemini API"""
    try:
        full_prompt = f"{context}\n\n{prompt}" if context else prompt
        response = st.session_state.model.generate_content(full_prompt)
        return response.text
    except Exception as e:
        return f"Error: {str(e)}"