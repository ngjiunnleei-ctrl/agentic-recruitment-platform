from fastapi import FastAPI

from backend.app.routes.candidates import router as candidate_router
from backend.app.routes.upload import router as upload_router

app = FastAPI(
    title="Agentic Recruitment Platform",
    version="1.0.0"
)

app.include_router(candidate_router)
app.include_router(upload_router)

@app.get("/")
def root():
    return {
        "message": "Agentic Recruitment Platform API is running"
    }


@app.get("/health")
def health_check():
    return {
        "status": "healthy"
    }
