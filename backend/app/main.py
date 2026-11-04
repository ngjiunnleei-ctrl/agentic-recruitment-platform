from fastapi import FastAPI

app = FastAPI(
    title="Agentic Recruitment platform",
    version="0.1.0",
)

@app.get("/")
def root():
    return {
        "message": "Agentic Recruitment platform API is running!"
            }

@app.get("/health")
def health_check():
    return {
        "status": "healthy"
            }
