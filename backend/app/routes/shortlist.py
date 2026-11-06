from fastapi import APIRouter

from backend.app.services.recruiter_copilot import (
    search_candidates
)

from backend.app.services.shortlist_agent import (
    generate_shortlist
)

router = APIRouter()


@router.post("/copilot/shortlist")
def create_shortlist(
    query: str
):

    matches = search_candidates(query)

    top_candidates = matches[:5]

    shortlist = generate_shortlist(
        query,
        top_candidates
    )

    return {
        "query": query,
        "shortlist": shortlist
    }