from backend.app.services.candidate_creator import (
    create_candidate_from_ai
)

candidate_data = {
    "full_name": "Manisha Tripathi",
    "current_title": "Senior Software Engineer",
    "current_company": "Credit Suisse",
    "education": "MS Quantitative Finance and Computer Science",
    "years_experience": 10,
    "skills": [
        "Python",
        "Java",
        "SQL",
        "MATLAB"
    ]
}

candidate = create_candidate_from_ai(
    candidate_data
)

print(candidate.id)
print(candidate.name)
