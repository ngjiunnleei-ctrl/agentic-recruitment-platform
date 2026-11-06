import os
import json

from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)


def extract_candidate_profile(resume_text: str):

    prompt = f"""
    Extract candidate information from this resume.

    Return ONLY valid JSON.

    {{
        "full_name": "",
        "current_title": "",
        "current_company": "",
        "education": "",
        "years_experience": 0,
        "skills": []
    }}

    Resume:

    {resume_text}
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

    content = response.choices[0].message.content

    print("\n==== RAW AI RESPONSE ====\n")
    print(content)
    print("\n=========================\n")

    return content
