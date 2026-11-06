from backend.app.services.embedding_service import (
    create_embedding
)

from backend.app.services.semantic_matcher import (
    cosine_similarity
)

from sqlalchemy import select

from backend.app.database.models import Candidate
from backend.app.database.session import SessionLocal


def search_candidates(
    recruiter_query: str
):

    db = SessionLocal()

    candidates = db.scalars(
        select(Candidate)
    ).all()

    query_embedding = create_embedding(
        recruiter_query
    )

    results = []

    for candidate in candidates:

        candidate_text = f"""
        {candidate.name}

        {candidate.current_title}

        {candidate.current_company}

        {candidate.skills}

        {candidate.education}
        """

        candidate_embedding = (
            create_embedding(
                candidate_text
            )
        )

        score = cosine_similarity(
            query_embedding,
            candidate_embedding
        )

        results.append(
            {
                "candidate_id":
                    candidate.id,

                "candidate_name":
                    candidate.name,

                "semantic_score":
                    score
            }
        )

    results.sort(
        key=lambda x: x["semantic_score"],
        reverse=True
    )

    return results