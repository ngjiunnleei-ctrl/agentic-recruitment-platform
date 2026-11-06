from backend.app.services.matching_engine import (
    calculate_match_score
)

candidate_skills = [
    "Python",
    "Java",
    "SQL",
    "MATLAB",
    "Linux"
]

required_skills = [
    "Python",
    "SQL",
    "Azure",
    "Databricks"
]

score = calculate_match_score(
    candidate_skills,
    required_skills
)

print(
    f"Match Score: {score}%"
)