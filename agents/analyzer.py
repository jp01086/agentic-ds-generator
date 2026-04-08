from groq import Groq
import os
from dotenv import load_dotenv

# Load the .env file
load_dotenv()

# Create Groq client
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def analyze_problem(problem):

    response = client.chat.completions.create(
        messages=[
            {"role": "system", "content": "You are an expert in algorithms and data structures."},
            {"role": "user", "content": f"Analyze this problem and explain what data structure would be suitable: {problem}"}
        ],
        model="llama-3.1-8b-instant"
    )

    return response.choices[0].message.content