from sqlalchemy import Column, Integer, String

from backend.app.database.base import Base


class Candidate(Base):
    __tablename__ = "candidates"

    id = Column(Integer, primary_key=True, index=True)

    name = Column(String, nullable=False)

    email = Column(String)

    phone = Column(String)

    nationality = Column(String)

    years_experience = Column(Integer)

    current_title = Column(String)

    current_company = Column(String)

    education = Column(String)

    skills = Column(String)

class Job(Base):
    __tablename__ = "jobs"

    id = Column(Integer, primary_key=True, index=True)

    job_title = Column(String)

    required_skills = Column(String)

    preferred_skills = Column(String)

    years_experience = Column(Integer)
    