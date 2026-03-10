import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)


def generate_plan(ability, history):

    wrong_topics = []

    for h in history:
        if not h["correct"]:
            wrong_topics.append(h["topic"])

    prompt = f"""
    Ability: {ability}
    Weak topics: {wrong_topics}

    Create 3 step study plan.
    """

    res = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[{"role": "user", "content": prompt}]
    )

    return res.choices[0].message.content