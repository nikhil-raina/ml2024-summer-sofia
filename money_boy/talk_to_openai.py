import os
from openai import OpenAI

def fetch_openai_response(data, user_query):
    client = OpenAI(api_key=os.getenv("OPENAI_MONEY_MAN_API_KEY"))

    context = "The following data is extracted from a Google Sheet:\n"
    for row in data:
        context += ", ".join(f"{key}: {value}" for key, value in row.items()) + "\n"

    messages = [
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": f"{context}\nUser query: {user_query}"},
    ]

    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=messages,
    )

    return completion.choices[0].message.content
