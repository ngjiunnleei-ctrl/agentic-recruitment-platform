import json
import os

from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)


def extract_job_profile(
    jd_text: str
):

    prompt = f"""
    Extract information from this job description.

    Return ONLY valid JSON.

    {{
        "job_title": "",
        "required_skills": [],
        "preferred_skills": [],
        "years_experience": 0
    }}

    Job Description:

    {jd_text}
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

    return json.loads(content)
