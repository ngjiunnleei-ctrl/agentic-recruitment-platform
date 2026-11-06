from backend.app.services.ai_jd_parser import (
    extract_job_profile
)

sample_jd = """
Senior Data Engineer

Requirements:
Python
SQL
Azure
Databricks

Preferred:
Snowflake
Terraform

Experience:
5 years
"""

result = extract_job_profile(
    sample_jd
)

print(result)
