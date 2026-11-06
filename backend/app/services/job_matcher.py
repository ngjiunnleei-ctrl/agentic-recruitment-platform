from sqlalchemy import select

from backend.app.database.models import (
    Candidate,
    Job
)

from backend.app.database.session import (
    SessionLocal
)

from backend.app.services.matching_engine import (
    calculate_match_score
)


def get_matches_for_job(
    job_id: int
):

    db = SessionLocal()

    job = db.scalar(
        select(Job).where(
            Job.id == job_id
        )
    )

    if not job:
        return []

    required_skills = (
        job.required_skills.split(",")
    )

    candidates = db.scalars(
        select(Candidate)
    ).all()

    results = []

    for candidate in candidates:

        candidate_skills = []

        if candidate.skills:

            candidate_skills = (
                candidate.skills.split(",")
            )

        score = calculate_match_score(
            candidate_skills,
            required_skills
        )

        results.append(
            {
                "candidate_id":
                    candidate.id,

                "candidate_name":
                    candidate.name,

                "score":
                    score
            }
        )

    results.sort(
        key=lambda x: x["score"],
        reverse=True
    )

    return results
