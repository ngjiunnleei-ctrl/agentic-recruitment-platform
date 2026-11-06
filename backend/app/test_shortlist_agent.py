from backend.app.services.shortlist_agent import (
    generate_shortlist
)

query = """
Senior Data Engineer with Python,
SQL and analytics experience.
"""

candidates = [
    {
        "name": "Manisha Tripathi",
        "title": "Senior Software Engineer",
        "skills": [
            "Python",
            "Java",
            "SQL",
            "MATLAB",
            "Linux"
        ]
    }
]

result = generate_shortlist(
    query,
    candidates
)

print(result)
