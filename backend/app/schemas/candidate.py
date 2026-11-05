from pydantic import BaseModel


class CandidateCreate(BaseModel):
    name: str
    email: str
    phone: str
    nationality: str
    years_experience: int


class CandidateResponse(CandidateCreate):
    id: int

    class Config:
        from_attributes = True
        