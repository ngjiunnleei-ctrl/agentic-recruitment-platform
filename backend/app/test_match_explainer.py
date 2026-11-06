from backend.app.services.match_explainer import (
    explain_match
)

candidate = """
Manisha Tripathi

Senior Software Engineer

Python
Java
SQL
MATLAB

Credit Suisse
"""

job = """
Senior Data Engineer

Python
SQL
Azure
Databricks
"""

result = explain_match(
    candidate,
    job
)

print(result)