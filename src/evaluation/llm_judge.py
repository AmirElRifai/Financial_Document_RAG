import os
from openai import OpenAI

client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))

def judge_answer(question, context, answer):

    prompt = f"""
You are evaluating the quality of an AI answer.

Question:
{question}

Context:
{context}

Answer:
{answer}

Determine if the answer is supported by the context.

Respond with:
CORRECT or INCORRECT

Then briefly explain why.
"""

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}]
    )

    return response.choices[0].message.content