from backend.app.database.models import Candidate
from backend.app.database.session import SessionLocal


def create_candidate_from_ai(
    candidate_data: dict
):

    db = SessionLocal()

    candidate = Candidate(
        name=candidate_data.get("full_name"),
        current_title=candidate_data.get("current_title"),
        current_company=candidate_data.get("current_company"),
        education=candidate_data.get("education"),
        years_experience=candidate_data.get(
            "years_experience", 0
        ),
        skills=",".join(
            candidate_data.get("skills", [])
        )
    )

    db.add(candidate)

    db.commit()

    db.refresh(candidate)

    return candidate
