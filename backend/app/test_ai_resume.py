from backend.app.services.ai_resume_parser import (
    extract_candidate_profile
)

sample_text = """
Manisha Tripathi

Senior Software Engineer

Credit Suisse

Skills:
Python
Java
SQL
MATLAB
Bloomberg
Linux

Education:
MS Quantitative Finance and Computer Science
"""

result = extract_candidate_profile(
    sample_text
)

print(result)
