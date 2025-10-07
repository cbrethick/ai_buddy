📚 AI-Powered Study Buddy
An intelligent Streamlit application that leverages Google's Gemini AI to provide comprehensive study assistance. Generate explanations, summarize notes, create flashcards, take quizzes, and chat with an AI study assistant - all in one place!

✨ Features
🎓 Concept Explainer
Get simple, easy-to-understand explanations for complex concepts

Includes definitions, key points, real-world examples, and common misconceptions

Perfect for breaking down difficult topics

📝 Notes Summarizer
Paste your study notes and get concise summaries

Extracts key points and main ideas

Structured output with clear headings and bullet points

🃏 Flashcard Generator
Create interactive flashcards for any topic

Automatically generates questions and answers

Expandable cards for easy studying

📊 Quiz Maker
Generate multiple-choice quizzes on any subject

Instant answer checking and score calculation

Great for self-assessment and exam preparation

💬 Study Chat Assistant
Interactive chat interface for study-related questions

Maintains conversation history

Context-aware responses tailored for learning

🚀 Installation
Prerequisites
Python 3.7 or higher

Google Gemini API key

Step-by-Step Setup
Clone or download the project files

bash
git clone <repository-url>
cd study_buddy_app
Install required packages

bash
pip install streamlit google-generativeai python-dotenv
Set up environment variables

Create a .env file in the project directory

Add your Gemini API key:

text
GEMINI_API_KEY=your_actual_api_key_here
Get your Gemini API key

Visit Google AI Studio

Create a new API key

Copy the key into your .env file

📁 Project Structure
text
study_buddy_app/
│
├── app.py          # Main Streamlit application & UI
├── utils.py        # API configuration & utility functions
├── features.py     # Study features & content parsing
├── .env           # Environment variables (create this)
├── requirements.txt # Dependencies
└── README.md       # This file
🎯 Usage
Run the application

bash
streamlit run app.py
Access the app

Open your web browser to the local URL shown in the terminal (typically http://localhost:8501)

Choose your study mode

Use the sidebar to navigate between different features

Enter your topic or notes in the provided text areas

Click the respective buttons to generate content

💡 Tips for Best Results
Be specific: Provide clear, detailed concepts or topics for better explanations

Use quality notes: Well-structured input notes yield better summaries

Break down complex topics: Use multiple sessions for large subjects

Experiment: Try different phrasings if you're not getting the desired results

Review generated content: Always verify AI-generated information for accuracy

🔧 Configuration
Model Options
The app currently uses gemini-2.5-pro. You can modify this in utils.py:

python
# In configure_gemini() function:
return genai.GenerativeModel('models/gemini-2.5-pro')  # or 'models/gemini-2.5-flash'
Customization
Modify prompts in features.py to tailor responses to your needs

Adjust the number of flashcards or quiz questions by editing the prompt templates

Customize the UI by modifying app.py

🛠️ Troubleshooting
Common Issues
API Key Error

Ensure your .env file is in the correct directory

Verify the API key is correctly formatted

Check that the key has proper permissions

Module Not Found

Run pip install -r requirements.txt to install all dependencies

Ensure all project files are in the same directory

Empty Responses

Check your internet connection

Verify the Gemini API service is available

Try simplifying your input prompts

📋 Requirements
Create a requirements.txt file with:

txt
streamlit>=1.28.0
google-generativeai>=0.3.0
python-dotenv>=1.0.0
Install with:

bash
pip install -r requirements.txt
🔒 Privacy & Security
API keys are stored locally in .env files

No data is permanently stored on external servers

Chat history is maintained only during the current session

Always follow your institution's policies regarding AI tool usage

🎓 Educational Use
This tool is ideal for:

Students preparing for exams

Learners exploring new subjects

Teachers creating study materials

Self-paced learning and revision

🤝 Contributing
Feel free to contribute by:

Adding new study features

Improving existing functionality

Enhancing the user interface

Fixing bugs and issues

📄 License
This project is for educational purposes. Please ensure compliance with Google's Gemini API terms of service.

🆘 Support
If you encounter issues:

Check the troubleshooting section above

Verify all installation steps were followed

Ensure your API key is valid and has sufficient quota

Check the Streamlit community forums for similar issues

Happy Studying! 📖✨
