from backend.app.services.candidate_creator import (
    create_candidate_from_ai
)

candidates = [

    {
        "full_name": "Manisha Tripathi",
        "current_title": "Senior Software Engineer",
        "current_company": "Credit Suisse",
        "education": "MS Quantitative Finance and Computer Science",
        "years_experience": 10,
        "skills": [
            "Python",
            "Java",
            "SQL",
            "MATLAB",
            "Bloomberg",
            "Linux"
        ]
    },

    {
        "full_name": "John Tan",
        "current_title": "Senior Data Engineer",
        "current_company": "DBS Bank",
        "education": "Bachelor of Computer Science",
        "years_experience": 8,
        "skills": [
            "Python",
            "SQL",
            "Azure",
            "Databricks",
            "Snowflake",
            "Spark"
        ]
    },

    {
        "full_name": "Sarah Lim",
        "current_title": "Cloud Architect",
        "current_company": "Accenture",
        "education": "Master of Information Systems",
        "years_experience": 12,
        "skills": [
            "Azure",
            "AWS",
            "Terraform",
            "Kubernetes",
            "Python"
        ]
    },

    {
        "full_name": "David Wong",
        "current_title": "DevOps Engineer",
        "current_company": "GovTech",
        "education": "Bachelor of Engineering",
        "years_experience": 7,
        "skills": [
            "Docker",
            "Kubernetes",
            "Azure",
            "Terraform",
            "Linux",
            "Python"
        ]
    },

    {
        "full_name": "Priya Nair",
        "current_title": "Data Scientist",
        "current_company": "Grab",
        "education": "Master of Data Science",
        "years_experience": 6,
        "skills": [
            "Python",
            "Machine Learning",
            "SQL",
            "Pandas",
            "TensorFlow",
            "Databricks"
        ]
    }

]

for candidate in candidates:
    create_candidate_from_ai(candidate)

print("Candidates seeded successfully")