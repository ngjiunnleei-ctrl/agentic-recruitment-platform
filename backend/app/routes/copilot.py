from fastapi import APIRouter

from backend.app.services.recruiter_copilot import (
    search_candidates
)

router = APIRouter()


@router.post("/copilot/search")
def copilot_search(
    query: str
):

    return search_candidates(query)