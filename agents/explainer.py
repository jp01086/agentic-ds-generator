from groq import Groq
import os

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def explain_rejection(problem, selected_ds):

    prompt = f"""
    Problem:
    {problem}

    Selected Data Structure:
    {selected_ds}

    Explain why the following data structures are NOT suitable:
    - Array
    - Linked List
    - Stack
    - Queue
    - Hash Table
    - Tree

    Give short bullet explanations.
    """

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role": "user", "content": prompt}]
    )

    return response.choices[0].message.content