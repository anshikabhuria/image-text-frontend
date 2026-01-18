from fastapi import APIRouter, UploadFile, File, Form
from app.schemas import UploadResponse
from app import crud

router = APIRouter(prefix="/upload", tags=["Upload"])

@router.post("/", response_model=UploadResponse)
def upload_image_and_text(
    image: UploadFile = File(...),
    text: str = Form(...)
):
    return crud.save_image_and_text(image, text)
