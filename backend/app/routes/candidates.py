from fastapi import APIRouter
from sqlalchemy import select

from backend.app.database.models import Candidate
from backend.app.database.session import SessionLocal
from backend.app.schemas.candidate import (
    CandidateCreate,
    CandidateResponse,
)

router = APIRouter()


@router.get("/candidates")
def get_candidates():

    db = SessionLocal()

    candidates = db.scalars(
        select(Candidate)
    ).all()

    return candidates


@router.post(
    "/candidates",
    response_model=CandidateResponse
)
def create_candidate(
    candidate: CandidateCreate
):

    db = SessionLocal()

    new_candidate = Candidate(
        name=candidate.name,
        email=candidate.email,
        phone=candidate.phone,
        nationality=candidate.nationality,
        years_experience=candidate.years_experience
    )

    db.add(new_candidate)
    db.commit()
    db.refresh(new_candidate)

    return new_candidate
