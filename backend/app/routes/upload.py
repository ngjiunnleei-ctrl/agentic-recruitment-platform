import os

from fastapi import APIRouter, UploadFile, File

from backend.app.services.resume_parser import (
    extract_text_from_pdf
)

router = APIRouter()

UPLOAD_FOLDER = "backend/uploads"

os.makedirs(
    UPLOAD_FOLDER,
    exist_ok=True
)


@router.post("/upload-resume")
async def upload_resume(
    file: UploadFile = File(...)
):

    file_path = os.path.join(
        UPLOAD_FOLDER,
        file.filename
    )

    contents = await file.read()

    with open(
        file_path,
        "wb"
    ) as f:

        f.write(contents)

    extracted_text = extract_text_from_pdf(
        file_path
    )

    return {
        "filename": file.filename,
        "status": "uploaded",
        "text_preview": extracted_text[:1000]
    }