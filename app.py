import streamlit as st
from utils import configure_gemini, generate_response
from features import (
    explain_concept, 
    summarize_notes, 
    generate_flashcards, 
    generate_quiz,
    parse_flashcards,
    parse_quiz
)

# Configure page
st.set_page_config(
    page_title="AI-Powered Study Buddy",
    page_icon="📚",
    layout="wide"
)

# Initialize session state
if 'model' not in st.session_state:
    st.session_state.model = configure_gemini()
if 'chat_history' not in st.session_state:
    st.session_state.chat_history = []
if 'flashcards' not in st.session_state:
    st.session_state.flashcards = []
if 'quizzes' not in st.session_state:
    st.session_state.quizzes = []

# Main UI
st.title("📚 AI-Powered Study Buddy")
st.markdown("Your personal AI assistant for learning and studying!")

# Sidebar
st.sidebar.title("Navigation")
app_mode = st.sidebar.radio(
    "Choose a mode:",
    ["Concept Explainer", "Notes Summarizer", "Flashcard Generator", "Quiz Maker", "Chat Assistant"]
)

# Concept Explainer
if app_mode == "Concept Explainer":
    st.header("🎓 Concept Explainer")
    st.write("Get simple explanations for complex concepts")
    
    concept = st.text_area("Enter a concept you want to understand:", 
                          placeholder="e.g., Photosynthesis, Quantum Physics, Machine Learning...")
    
    if st.button("Explain Concept") and concept:
        with st.spinner("Generating explanation..."):
            explanation = explain_concept(concept)
            st.subheader(f"Explanation of: {concept}")
            st.markdown(explanation)

# Notes Summarizer
elif app_mode == "Notes Summarizer":
    st.header("📝 Notes Summarizer")
    st.write("Paste your study notes and get a concise summary")
    
    notes = st.text_area("Paste your notes here:", height=200,
                        placeholder="Enter your study notes...")
    
    if st.button("Summarize Notes") and notes:
        with st.spinner("Summarizing your notes..."):
            summary = summarize_notes(notes)
            st.subheader("Summary")
            st.markdown(summary)

# Flashcard Generator
elif app_mode == "Flashcard Generator":
    st.header("🃏 Flashcard Generator")
    st.write("Generate flashcards for any topic")
    
    topic = st.text_input("Enter a topic for flashcards:")
    
    col1, col2 = st.columns([1, 4])
    
    with col1:
        if st.button("Generate Flashcards") and topic:
            with st.spinner("Creating flashcards..."):
                st.session_state.flashcards = generate_flashcards(topic)
    
    # Display flashcards
    if st.session_state.flashcards:
        st.subheader(f"Flashcards for: {topic}")
        
        for i, card in enumerate(st.session_state.flashcards, 1):
            with st.expander(f"Card {i}: {card['question'][:50]}..."):
                st.write("**Question:**", card['question'])
                st.write("**Answer:**", card['answer'])

# Quiz Maker
elif app_mode == "Quiz Maker":
    st.header("📊 Quiz Maker")
    st.write("Test your knowledge with AI-generated quizzes")
    
    topic = st.text_input("Enter a topic for the quiz:")
    
    if st.button("Generate Quiz") and topic:
        with st.spinner("Creating quiz..."):
            st.session_state.quizzes = generate_quiz(topic)
    
    # Display quiz
    if st.session_state.quizzes:
        st.subheader(f"Quiz: {topic}")
        
        user_answers = {}
        score = 0
        
        for i, question in enumerate(st.session_state.quizzes, 1):
            st.write(f"**{i}. {question['question']}**")
            
            user_answer = st.radio(
                f"Select your answer for question {i}:",
                options=list(question['options'].keys()),
                format_func=lambda x: f"{x}) {question['options'][x]}",
                key=f"q_{i}"
            )
            user_answers[i] = user_answer
            
            if st.button(f"Check Answer {i}", key=f"check_{i}"):
                if user_answer == question['correct']:
                    st.success("✅ Correct!")
                else:
                    st.error(f"❌ Incorrect. The correct answer is {question['correct']}) {question['options'][question['correct']]}")
        
        if st.button("Calculate Total Score"):
            score = sum(1 for i, q in enumerate(st.session_state.quizzes, 1) 
                       if user_answers.get(i) == q['correct'])
            st.success(f"Your score: {score}/{len(st.session_state.quizzes)}")

# Chat Assistant
elif app_mode == "Chat Assistant":
    st.header("💬 Study Chat Assistant")
    st.write("Chat with your AI study buddy about any topic")
    
    # Display chat history
    for message in st.session_state.chat_history:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])
    
    # Chat input
    if prompt := st.chat_input("Ask your study question..."):
        # Add user message to chat history
        st.session_state.chat_history.append({"role": "user", "content": prompt})
        
        # Display user message
        with st.chat_message("user"):
            st.markdown(prompt)
        
        # Generate and display AI response
        with st.chat_message("assistant"):
            with st.spinner("Thinking..."):
                response = generate_response(
                    f"Act as a helpful study assistant. Answer the student's question clearly and simply: {prompt}"
                )
                st.markdown(response)
        
        # Add AI response to chat history
        st.session_state.chat_history.append({"role": "assistant", "content": response})

# Footer
st.markdown("---")
st.markdown("### 💡 Tips for better results:")
st.markdown("""
- Be specific in your questions
- Provide clear context when needed
- Break down complex topics into smaller parts
- Use the different tools for different study needs
""")