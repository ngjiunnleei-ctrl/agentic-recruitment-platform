from backend.app.database.connection import engine
from backend.app.database.base import Base
from backend.app.database.models import Candidate, Job  

Base.metadata.create_all(bind=engine)

print("TABLES CREATED SUCCESSFULLY")
