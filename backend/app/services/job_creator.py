from backend.app.database.models import Job
from backend.app.database.session import SessionLocal


def create_job_from_ai(
    job_data: dict
):

    db = SessionLocal()

    job = Job(
        job_title=job_data["job_title"],
        required_skills=",".join(
            job_data["required_skills"]
        ),
        preferred_skills=",".join(
            job_data["preferred_skills"]
        ),
        years_experience=job_data[
            "years_experience"
        ]
    )

    db.add(job)

    db.commit()

    db.refresh(job)

    return job
