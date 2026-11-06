from fastapi import APIRouter
from openai import OpenAI
from dotenv import load_dotenv

import os

load_dotenv()

router = APIRouter()

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)


@router.post("/copilot")
def recruiter_copilot(
    query: str
):

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {
                "role": "system",
                "content": """
                You are an expert technology recruiter.
                Help identify candidates and explain suitability.
                """
            },
            {
                "role": "user",
                "content": query
            }
        ]
    )

    return {
        "response":
            response.choices[0].message.content
    }