import os

from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)


def generate_shortlist(
    recruiter_query: str,
    candidates: list
):

    prompt = f"""
    Act as a senior technology recruiter.

    Query:

    {recruiter_query}

    Candidates:

    {candidates}

    Produce a ranked shortlist.

    Explain why each candidate is relevant.

    Keep the response concise.
    """

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0
    )

    return response.choices[0].message.content