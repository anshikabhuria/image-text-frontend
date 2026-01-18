from pydantic import BaseModel

class UploadResponse(BaseModel):
    id: int
    text: str
    image_path: str
