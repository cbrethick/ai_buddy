import re
from utils import generate_response

def explain_concept(concept):
    """Explain a concept in simple terms"""
    prompt = f"""
    Explain the following concept in simple, easy-to-understand terms as if you're explaining to a student:
    Concept: {concept}
    
    Please provide:
    1. A simple definition
    2. Key points in bullet form
    3. A real-world example
    4. Common misconceptions (if any)
    
    Keep it concise and student-friendly.
    """
    return generate_response(prompt)

def summarize_notes(notes):
    """Summarize study notes"""
    prompt = f"""
    Please summarize the following study notes into key points. 
    Focus on the main ideas and important details:
    
    {notes}
    
    Provide the summary in a structured format with clear headings and bullet points.
    """
    return generate_response(prompt)

def generate_flashcards(topic):
    """Generate flashcards for a topic"""
    prompt = f"""
    Create 10 flashcards for the topic: {topic}
    
    Format each flashcard as:
    Question: [question]
    Answer: [answer]
    
    Separate each flashcard with "---"
    Make sure the questions cover different aspects of the topic.
    """
    response = generate_response(prompt)
    return parse_flashcards(response)

def parse_flashcards(flashcard_text):
    """Parse flashcard text into structured format"""
    flashcards = []
    cards = flashcard_text.split('---')
    
    for card in cards:
        if 'Question:' in card and 'Answer:' in card:
            question_match = re.search(r'Question:\s*(.*?)(?=Answer:|$)', card, re.DOTALL)
            answer_match = re.search(r'Answer:\s*(.*?)(?=Question:|$)', card, re.DOTALL)
            
            if question_match and answer_match:
                flashcards.append({
                    'question': question_match.group(1).strip(),
                    'answer': answer_match.group(1).strip()
                })
    
    return flashcards

def generate_quiz(topic):
    """Generate a quiz for a topic"""
    prompt = f"""
    Create a 5-question multiple choice quiz about: {topic}
    
    Format each question as:
    Q[number]: [question]
    A) [option A]
    B) [option B]
    C) [option C]
    D) [option D]
    Correct: [correct letter]
    
    Separate each question with "---"
    """
    response = generate_response(prompt)
    return parse_quiz(response)

def parse_quiz(quiz_text):
    """Parse quiz text into structured format"""
    questions = []
    quiz_blocks = quiz_text.split('---')
    
    for block in quiz_blocks:
        if 'Q' in block and 'A)' in block:
            question_match = re.search(r'Q\d+:\s*(.*?)(?=A\)|$)', block, re.DOTALL)
            options_match = re.findall(r'([A-D])\)\s*(.*?)(?=[A-D]\)|Correct:|$)', block)
            correct_match = re.search(r'Correct:\s*([A-D])', block)
            
            if question_match and options_match and correct_match:
                questions.append({
                    'question': question_match.group(1).strip(),
                    'options': {opt[0]: opt[1].strip() for opt in options_match},
                    'correct': correct_match.group(1).strip()
                })
    
    return questions