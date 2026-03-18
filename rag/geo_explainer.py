from rag.embedding_store import search
from openai import OpenAI
import os

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def explain(rainfall, traffic, distance, risk):
    context = search("risk factors")

    prompt = f"""
    Context: {context}
    Data:
    Rainfall: {rainfall}
    Traffic: {traffic}
    Distance: {distance}
    Risk: {risk}

    Explain why this region is risky.
    """

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}]
    )

    return response.choices[0].message.content
