from backend.app.services.job_matcher import (
    get_matches_for_job
)

matches = get_matches_for_job(1)

for match in matches:

    print(match)