from backend.app.services.job_creator import (
    create_job_from_ai
)

job_data = {
    "job_title": "Senior Data Engineer",
    "required_skills": [
        "Python",
        "SQL",
        "Azure",
        "Databricks"
    ],
    "preferred_skills": [
        "Snowflake"
    ],
    "years_experience": 5
}

job = create_job_from_ai(
    job_data
)

print(job.id)
print(job.job_title)
print(job.required_skills)
print(job.preferred_skills)
print(job.years_experience)
