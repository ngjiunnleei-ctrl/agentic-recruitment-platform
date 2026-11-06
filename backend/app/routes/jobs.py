from fastapi import APIRouter

from backend.app.services.job_matcher import (
    get_matches_for_job
)

router = APIRouter()


@router.get("/jobs/{job_id}/matches")
def get_job_matches(
    job_id: int
):
    return get_matches_for_job(job_id)