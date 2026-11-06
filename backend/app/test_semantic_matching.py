from backend.app.services.embedding_service import (
    create_embedding
)

from backend.app.services.semantic_matcher import (
    cosine_similarity
)

candidate_profile = """
Senior Software Engineer

Python
SQL
Java
Linux

Credit Suisse
"""

job_description = """
Senior Data Engineer

Python
SQL
Azure
Databricks
"""

candidate_embedding = create_embedding(
    candidate_profile
)

job_embedding = create_embedding(
    job_description
)

score = cosine_similarity(
    candidate_embedding,
    job_embedding
)

print(
    f"Semantic Match Score: {score}%"
)