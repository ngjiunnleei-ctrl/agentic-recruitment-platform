# backend/app/test_openai.py

import os
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")

if api_key:
    print("API Key Loaded Successfully")
    print(api_key[:15] + "...")
else:
    print("OPENAI_API_KEY not found")
    