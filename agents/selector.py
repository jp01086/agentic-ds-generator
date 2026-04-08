from groq import Groq
import os

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def select_data_structure(analysis):

    response = client.chat.completions.create(
        messages=[
            {"role": "system", "content": "You are an expert data structures selector. Return ONLY the name of the best data structure."},
            {"role": "user", "content": f"Based on this analysis, which data structure is best? {analysis}"}
        ],
        model="llama-3.3-70b-versatile"
    )

    ds = response.choices[0].message.content.strip().lower()

    return ds